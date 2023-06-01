"""
MIT License

Copyright (c) 2018 Rahul Sengottuvelu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import json
import re
from termcolor import colored
from typing import Any, Dict, List, Optional, Union

import openai


GENERATION_MARKER = "|GENERATION|"


class JsonformerNoTokens:
    value: Dict[str, Any] = {}

    def __init__(
        self,
        model: object,
        json_schema: Dict[str, Any],
        prompt: str,
        text: Optional[str] = None,
        debug: bool = False,
        max_array_length: int = 10,
        max_number_tokens: int = 6,
        temperature: float = 0.1,
        max_string_token_length: int = 10,
    ):
        self.model = model
        self.json_schema = json_schema
        self.prompt = prompt
        self.text = text

        self.generation_marker = "|GENERATION|"
        self.debug_on = debug
        self.max_array_length = max_array_length
        self.max_number_tokens = max_number_tokens
        self.temperature = temperature
        self.max_string_token_length = max_string_token_length

    def debug(self, *args, **kwargs):
        if self.debug_on:
            print(*args, **kwargs)

    def generate_number(self, temperature: Union[float, None] = None, iterations=0):
        prompt = self.get_prompt()
        self.debug("[generate_number] prompt", prompt)
        
        response = self.model.generate(
            prompt,
            max_new_tokens=self.max_number_tokens,
            stop=['",'],
            temperature=temperature or self.temperature,
        )
        self.debug("[generate_number] response", response)

        try:
            numbers = re.finditer(r"\d+(\.\d+)*", response)
            number = next(numbers).group(0)
            if "." in number:
                return float(number)
            else:
                return int(number)
        except (ValueError, StopIteration):
            try:
                pattern = [r"NA", r"NAN", r"NaN", r"nan"]
                regex = re.compile(r'\b(' + '|'.join(pattern) + r')\b')
                number = [m.group() for m in regex.finditer(response)]
                output = number
                return output[0]
            except (ValueError, StopIteration):          
                self.debug(f"[generate_number] FAILED")
                if iterations > 3:
                    raise ValueError("Failed to generate a valid number")
                return self.generate_number(
                    temperature=self.temperature * 1.3, iterations=iterations + 1
                )

    def generate_boolean(self) -> bool:
        prompt = self.get_prompt()
        self.debug("[generate_boolean] prompt", prompt)

        next_most_likely_token = self.model.get_next_most_likely_token(prompt)

        if next_most_likely_token.lower() in ["true", "1"]:
            return True
        elif next_most_likely_token.lower() in ["false", "0"]:
            return False
        else:
            print("Failed to generate a valid boolean value")
            return None

    def generate_string(self) -> str:
        prompt = self.get_prompt()
        self.debug("[generate_string] prompt", prompt)
        
        response = self.model.generate(
            prompt,
            max_new_tokens=self.max_string_token_length,
            stop=['",'],
            temperature=self.temperature,
        )

        self.debug("[generate_string] response", response)
        split = response.split('"')
        assert len(split) >= 2
        return split[1].strip()

    def generate_object(
        self, 
        properties: Dict[str, Any], 
        obj: Dict[str, Any],
    ) -> Dict[str, Any]:
        # self.debug("[generate_object] properties", properties)
        for key, schema in properties.items():
            obj[key] = self.generate_value(schema, obj, key)
        return obj

    def generate_value(
        self,
        schema: Dict[str, Any],
        obj: Union[Dict[str, Any], List[Any]],
        key: Union[str, None] = None,
    ) -> Any:
        schema_type = schema["type"]
        if schema_type == "number":
            if key:
                obj[key] = self.generation_marker
            else:
                obj.append(self.generation_marker)
            return self.generate_number()
        elif schema_type == "boolean":
            if key:
                obj[key] = self.generation_marker
            else:
                obj.append(self.generation_marker)
            return self.generate_boolean()
        elif schema_type == "string":
            if key:
                obj[key] = self.generation_marker
            else:
                obj.append(self.generation_marker)
            return self.generate_string()
        elif schema_type == "array":
            new_array = []
            obj[key] = new_array
            return self.generate_array(schema["items"], new_array)
        elif schema_type == "object":
            new_obj = {}
            if key:
                obj[key] = new_obj
            else:
                obj.append(new_obj)
            return self.generate_object(schema["properties"], new_obj)
        else:
            raise ValueError(f"Unsupported schema type: {schema_type}")

    def generate_array(
        self, 
        item_schema: Dict[str, Any], 
        obj: Dict[str, Any]
    ) -> list:
        for _ in range(self.max_array_length):
            # forces array to have at least one element
            element = self.generate_value(item_schema, obj)
            obj[-1] = element

            obj.append(self.generation_marker)
            input_prompt = self.get_prompt()
            obj.pop()
            next_most_likely_token = self.model.get_next_most_likely_token(input_prompt)
            if next_most_likely_token == "]":
                break
        return obj

    def get_prompt(self):
        template = """{prompt}\n{text}\nOutput result in the following JSON schema format, one value at a time, 
        do not continue the JSON:\n{schema}\nResult: {progress}"""
        progress = json.dumps(self.value)
        gen_marker_index = progress.find(f'"{self.generation_marker}"')
        if gen_marker_index != -1:
            progress = progress[:gen_marker_index]
        else:
            raise ValueError("Failed to find generation marker")

        prompt = template.format(
            prompt=self.prompt,
            text=self.text,
            schema=json.dumps(self.json_schema),
            progress=progress,
        )
        return prompt

    def __call__(self) -> Dict[str, Any]:
        self.value = {}
        generated_data = self.generate_object(self.json_schema["properties"], self.value)
        return generated_data


class OpenAIModel:
    def __init__(self, model_id: str = "text-curie-001", debug: bool = False):
        self.model_id = model_id
        self.debug_on = debug

    def __request(
        self,
        prompt: str,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        logprobs: Optional[int] = None,
        **kwargs,
    ):
        response = openai.Completion.create(
            model=self.model_id,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_new_tokens,
            logprobs=logprobs,
        )
        self.debug(response)
        return response

    def __clean_initial_new_lines(self, text: str):
        # models often start responses with new lines
        while text.startswith("\n"):
            text = text[1:]
        return text

    def debug(self, *args, **kwargs):
        if self.debug_on:
            print(*args, **kwargs)

    def generate(
        self,
        prompt: str,
        max_new_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs,
    ):
        response = self.__request(prompt, max_new_tokens=max_new_tokens, temperature=temperature)
        return self.__clean_initial_new_lines(response.choices[0].text)

    def get_next_most_likely_token(
        self,
        prompt: str,
    ):
        response = self.__request(prompt, logprobs=1)
        for obj in response.choices[0].logprobs.top_logprobs:
            # sorted from the most likely like so: [{"token": "logprob"}]
            if "\n" in obj:
                continue
            return list(obj.keys())[0]
      

def highlight_values(value):
    def recursive_print(obj, indent=0, is_last_element=True):
        if isinstance(obj, dict):
            print("{")
            last_key = list(obj.keys())[-1]
            for key, value in obj.items():
                print(f"{' ' * (indent + 2)}{key}: ", end="")
                recursive_print(value, indent + 2, key == last_key)
            print(f"{' ' * indent}}}", end=",\n" if not is_last_element else "\n")
        elif isinstance(obj, list):
            print("[")
            for index, value in enumerate(obj):
                print(f"{' ' * (indent + 2)}", end="")
                recursive_print(value, indent + 2, index == len(obj) - 1)
            print(f"{' ' * indent}]", end=",\n" if not is_last_element else "\n")
        else:
            if isinstance(obj, str):
                obj = f'"{obj}"'
            print(colored(obj, "light_blue"), end=",\n" if not is_last_element else "\n")

    recursive_print(value) 
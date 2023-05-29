# LLMsTablesToJson

#### Generate structured JSON from tables contained in scientific articles


## 🚀 Installation

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/vgvinter/LLMsTablesToJson.gitt
```


## :memo: Description

The input to obtain the JSON format of a table is the DOI identifier of a research paper and the table number in the article.

Using the `selenium` library, the HTML code of the table contained in the paper is extracted. Then, using the OpenAI’s models structured JSON is generated from the table HTML.

The code to extract the table HTML from the paper DOI is in `html_table.py`. The code to generate JSON using OpenAI’s models is in `jsonformer_non_tokens.py` (based on: https://github.com/1rgs/jsonformer and https://github.com/martinezpl/jsonformer/tree/add-openai).


### Examples

The generation of structured JSON for different tables extracted from research papers on several topics is shown in Jupyter Notebooks in the main directory.

The HTML code for the example tables is in the `html_tables` folder. The JSON schemas given to the model to generate valid JSON are in the `json_schemas` folder. The generated JSON for all the examples are in the `structured_json_folder`.

The code of a demo app to visualize the results is available in `app.py`.


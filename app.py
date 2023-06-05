import json

import IPython
from IPython.display import HTML
import streamlit as st


def main():

    st.set_page_config(
        page_title="LLMs: JSON structured tables from scientific papers", 
        layout="wide"
    )
    st.title(":page_facing_up: LLMs: JSON structured tables from scientific papers")

    st.markdown("""
        <style>
                .block-container {
                    padding-top: 2rem;
                }
        </style>
        """, unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns([1,12,1])

    with col2: 
        st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                font-size: 24px;">DOI of the article containing the table:</p>', unsafe_allow_html=True)
         
        table = st.selectbox(
            "Choose a DOI",
            ("10.1016/j.jece.2023.109643", "10.1021/ja4045289", "10.1016/j.est.2023.107335", 
            "10.1021/acs.energyfuels.1c02406", "10.1016/j.enconman.2018.09.020", 
            "10.1039/D3NJ00316G", "10.1016/j.ceramint.2019.11.066", "10.1021/ja4045289_wrong schema"), 
            label_visibility="collapsed"
        )


        if table == "10.1016/j.jece.2023.109643":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Properties of activated carbons for CO<sub>2</sub> adsorption:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_carbonsCO2ads.txt", 'r') as file:
                html_table_carbonsCO2ads = file.read()
                file.close()
            st.write(HTML(html_table_carbonsCO2ads))

            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_carbonsCO2ads.json") as file:
                    json_table_carbonsCO2ads = json.load(file)
                    file.close()
                st.json(json_table_carbonsCO2ads)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_openai_results/davinci_carbonsCO2ads.json") as file:
                    davinci_carbonsCO2ads = json.load(file)
                    file.close()
                st.json(davinci_carbonsCO2ads)


        if table == "10.1021/ja4045289":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">MOFs properties:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_MOFproperties.txt", 'r') as file:
                html_table_MOFproperties = file.read()
                file.close()
            st.write(HTML(html_table_MOFproperties))
            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_MOFproperties.json") as file:
                    json_table_MOFproperties = json.load(file)
                    file.close()
                st.json(json_table_MOFproperties)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_openai_results/davinci_MOFproperties.json") as file:
                    davinci_MOFproperties = json.load(file)
                    file.close()
                st.json(davinci_MOFproperties)


        if table == "10.1016/j.est.2023.107335":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Supercapacitor performance of 2D nanocomposite materials:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_supercapacitor.txt", 'r') as file:
                html_table_supercapacitor = file.read()
                file.close()
            st.write(HTML(html_table_supercapacitor))
            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_supercapacitor.json") as file:
                    json_table_supercapacitor = json.load(file)
                    file.close()
                st.json(json_table_supercapacitor)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_openai_results/davinci_supercapacitor.json") as file:
                    davinci_supercapacitor = json.load(file)
                    file.close()
                st.json(davinci_supercapacitor)


        if table == "10.1021/acs.energyfuels.1c02406":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Catalysts for CO<sub>2</sub> Fischer–Tropsch conversion to liquid fuels:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_catalystCO2.txt", 'r') as file:
                html_table_catalystCO2 = file.read()
                file.close()
            st.write(HTML(html_table_catalystCO2))
            st.write("")
            st.write("")
            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_catalystCO2.json") as file:
                    json_table_catalystCO2 = json.load(file)
                    file.close()
                st.json(json_table_catalystCO2)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_openai_results/davinci_catalystCO2.json") as file:
                    davinci_catalystCO2 = json.load(file)
                    file.close()
                st.json(davinci_catalystCO2)


        if table == "10.1016/j.enconman.2018.09.020":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Biomass properties:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_biomass.txt", 'r') as file:
                html_table_biomass = file.read()
                file.close()
            st.write(HTML(html_table_biomass))
            st.write("")
            st.write("")
            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_biomass.json") as file:
                    json_table_biomass = json.load(file)
                    file.close()
                st.json(json_table_biomass)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                with open("structured_openai_results/davinci_biomass.json") as file:
                    davinci_biomass = json.load(file)
                    file.close()
                st.json(davinci_biomass)

        
        if table == "10.1039/D3NJ00316G":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Ni-doped ceria anode materials for SOFCs:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_anodesSOFCs.txt", 'r') as file:
                html_table_anodesSOFCs = file.read()
                file.close()
            st.write(HTML(html_table_anodesSOFCs))
            st.write("")
            st.write("")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">JSON with the standard promt</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: "Generate an object with the following schema \
                            extracting the information from the provided table in html code:"</p>', 
                            unsafe_allow_html=True)
                st.write("")
                st.write("")
                with open("structured_jsonformer_results/json_table_anodesSOFCs_wrong.json") as file:
                    json_table_anodesSOFCs_wrong = json.load(file)
                    file.close()
                st.json(json_table_anodesSOFCs_wrong)
            with col2:
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">JSON with the improved promt</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: ""Generate an object with the following schema extracting \
                            the information from the provided table in html code (if you find numbers as \
                            1.025 × 10&lt;sub&gt;-3&lt;/sub&gt;</code>, this means 1.025e-3):"</p>',
                            unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_anodesSOFCs.json") as file:
                    json_table_anodesSOFCs = json.load(file)
                    file.close()
                st.json(json_table_anodesSOFCs)
            with col3:
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">standard promt</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: "Generate a JSON object extracting the information \
                            from this table in html code:"</p>', 
                            unsafe_allow_html=True)
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                with open("structured_openai_results/davinci_anodesSOFCs.json") as file:
                    davinci_anodesSOFCs = json.load(file)
                    file.close()
                st.json(davinci_anodesSOFCs)
        
        if table == "10.1016/j.ceramint.2019.11.066":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">Perovskite-structured cathode materials for SOFCs:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_perovskiteSOFCs.txt", 'r') as file:
                    html_table_carbonsCO2ads = file.read()
                    file.close()
            st.write(HTML(html_table_carbonsCO2ads))
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">JSON with the standard promt (and too low value of \
                            <code>max_string_token_length</code> argument)</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: "Generate an object with the following schema \
                            extracting the information from the provided table in html code:"</p>', 
                            unsafe_allow_html=True)
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                with open("structured_jsonformer_results/json_table_perovskiteSOFCs.json") as file:
                    json_table_perovskiteSOFCs = json.load(file)
                    file.close()
                st.json(json_table_perovskiteSOFCs)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">JSON with the improved promt (and higher value of \
                            <code>max_string_token_length</code> argument)</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: ""Generate an object with the following schema extracting \
                            the information from the provided table in html code (if you find numbers as \
                            1.025 × 10&lt;sub&gt;-3&lt;/sub&gt;</code>, this means 1.025e-3), decode Unicode \
                            characters in your response:"</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_perovskiteSOFCs_names_regular.json") as file:
                    json_table_perovskiteSOFCs_names_regular = json.load(file)
                    file.close()
                st.json(json_table_perovskiteSOFCs_names_regular)            
            with col3:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; color:steelblue; \
                            font-size: 18px;">standard promt</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 14px;">prompt: "Generate a JSON object extracting the information \
                            from this table in html code:"</p>', unsafe_allow_html=True)
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                with open("structured_openai_results/davinci_perovskiteSOFCs.json") as file:
                    davinci_carbonsCO2ads = json.load(file)
                    file.close()
                st.json(davinci_carbonsCO2ads)


        
        if table == "10.1021/ja4045289_wrong schema":
            st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:steelblue; \
                        font-size: 22px;">MOFs properties with a wrong schema provided to the model:</p>', 
                        unsafe_allow_html=True)
            with open("html_tables/html_table_MOFproperties.txt", 'r') as file:
                html_table_MOFproperties = file.read()
                file.close()
            st.write(HTML(html_table_MOFproperties))
            col1, col2 = st.columns([1,1])
            with col1:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">jsonformer + OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 16px;">(values in table are inserted in the provided \
                            wrong schema)</p>', unsafe_allow_html=True)
                with open("structured_jsonformer_results/json_table_MOFproperties_wrong_schema.json") as file:
                    json_table_MOFproperties_wrong_schema = json.load(file)
                    file.close()
                st.json(json_table_MOFproperties_wrong_schema)
            with col2:
                st.write("")
                st.markdown('<p style="font-family: sans-serif; font-weight: bold; color:steelblue; \
                            font-size: 20px;">OpenAI model</p>', unsafe_allow_html=True)
                st.markdown('<p style="font-family: sans-serif; font-weight: normal; color:grey; \
                            font-size: 16px;">(new schema is created following the table)</p>', 
                            unsafe_allow_html=True)
                with open("structured_openai_results/davinci_MOFproperties_wrong_schema.json") as file:
                    davinci_MOFproperties_wrong_schema = json.load(file)
                    file.close()
                st.json(davinci_MOFproperties_wrong_schema)


if __name__ == "__main__":
    main()

# Notes summariser using LLM

This app helps summarise large text files using RecursiveTextSplit method under langchain. You also can access the analytics of the LLM using langchain's API. 

## Installation

1. Clone the repository.
2. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the necessary environment variables by creating a `.env` file with the following keys:
   - `LANGCHAIN_TRACING_V2` as `true`
   - `LANGCHAIN_API_KEY`
   - `OPENAI_API_KEY`

## Local Usage

1. Run the Streamlit app by executing:
   ```bash
   streamlit run app.py
   ```
   or if you have ollama llama3 installed locally then you can use 
   ```
   streamlit run app_ollama.py
   ```
2. Paste the content you want to summarize in the text area.
3. Click the "Summarize" button to generate a summary

## Exposing APIs

1. Run app.py file under api folder using ``fastapi dev app.py`` 
2. Check the API payload structure on ``http://127.0.0.1:8000/docs`` 



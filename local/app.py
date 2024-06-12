from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
print(os.environ["OPENAI_API_KEY"])
promt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a document summariser. Please summarise the document keeping the summary short and to the point"),
        ("user", "Question:{question}")
    ]
)




llm=ChatOpenAI(model='gpt-3.5-turbo')
output_parser=StrOutputParser()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len, 
    separators=[
        "\n\n",
        "\n"
    ]
    )

def summarize_text(input_text):
    segments = text_splitter.split_text(input_text)
    summaries = []
    for segment in segments:
        response = promt | llm | output_parser
        summary = response.invoke({'question': segment})
        summaries.append(summary)
    return " ".join(summaries)




st.title("Notes Summariser App using chatGPT") 
st.markdown(
    f"""
    <style>
    .reportview-container .main .block-container{{
        max-width: 1000px;
    }}
    .reportview-container .main .block-container .stTextInput {{
        resize: vertical;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
input_text=st.text_area("Paste the content to summarise")

if st.button('Summarize'):
    st.write(summarize_text(input_text))

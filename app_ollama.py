from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os 
from dotenv import load_dotenv

os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

promt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a document summariser. Please summarise the document keeping the summary short and to the point"),
        ("user", "Question:{question}")
    ]
)

st.title("Notes Summariser App using Ollama") 
input_text=st.text_input("Paste the content to summarise")

llm=Ollama(model='llama3')
output_parser=StrOutputParser()

chain= promt | llm | output_parser

if input_text: 
    st.write(chain.invoke({'question': input_text}))
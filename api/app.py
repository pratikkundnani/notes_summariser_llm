from fastapi import FastAPI
from pydantic import BaseModel
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
import uvicorn 
import os 
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


app = FastAPI()

class Notes(BaseModel):
    text: str
    model: str

@app.post("/summarize")
async def summarize(notes: Notes):  
    promt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a document summariser. Please summarise the document keeping the summary short and to the point"),
            ("user", "Text to summarise:{notes}")
        ]
    )
    print("control reached")
    print(notes.model)
    if notes.model == 'chatgpt':
        llm=ChatOpenAI(model='gpt-3.5-turbo')
    else:
        llm=Ollama(model='llama3')
    
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
    segments = text_splitter.split_text(notes.text)
    summaries = []
    for segment in segments:
        response = promt | llm | output_parser
        summary = response.invoke({'notes': segment})
        summaries.append(summary)
    return " ".join(summaries)

# Q and A system using Gemini langchain


import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Now we can instantiate our model object and generate chat completions:
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a chatbot"),
        ("human","Question:{question}")
    ]
)



st.title('Langchain With Gemini Q and A system ')
input_text=st.text_input("Enter your question here")


output_parser=StrOutputParser() #to get o/p in more readable form

chain=prompt|llm|output_parser   # how the process should work.  first prompt - user will write the question - it 
#will be passed to llm and then llm will produce the output which we see on screen.
  
if input_text:
    st.write(chain.invoke({'question':input_text})) 


    
# To run this code, write-  streamlit run gemini_app_qa.py
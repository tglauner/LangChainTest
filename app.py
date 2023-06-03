# app.py
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

print("Start")
load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.9) 
text = "How are you?"

print(llm(text))

print("End")

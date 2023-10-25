# app.py
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader

print("Start")
load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")) 
#text = "How are you?"
#print(llm(text))

# load document
loader = PyPDFLoader("LEH The Swap Curve.pdf")
documents = loader.load() 

# ask document some questions
chain = load_qa_chain(llm=llm, chain_type="map_reduce")
query = "Summarize the document in 100 words"
print("Query:"+query)
print(chain.run(input_documents=documents, question=query),"\n")
query = "What are the main ten points of the document?"
print("Query:"+query)
print(chain.run(input_documents=documents, question=query),"\n")
print("End")

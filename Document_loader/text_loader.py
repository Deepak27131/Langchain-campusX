from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7, 
)


prompt = PromptTemplate(
    template = "Write a summary for the following poen - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')

doc = loader.load()

print(type(doc))

print(len(doc))


print(doc[0].page_content)

print(doc[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':doc[0].page_content}))
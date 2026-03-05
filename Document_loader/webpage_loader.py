from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader,WebBaseLoader
from bs4 import BeautifulSoup
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
    template = "Answer the follwoing question \n {question} form the following text - \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()


url = "https://www.flipkart.com/nivea-nourishing-lotion-body-milk-deep-moisture-serum-2x-almond-oil/p/itmfa8ac85ac8019?pid=MSCGVE5W4ZNZ7EGJ&lid=LSTMSCGVE5W4ZNZ7EGJB3MARS&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6ImhwIiwibWlkIjoicGVyc29uYWxpc2VkUmVjb21tZW5kYXRpb24vcDJwLXNhbWUifQ%3D%3D&pageUID=1772013928309"

loader = WebBaseLoader(url)

doc = loader.load()

chain = prompt | model | parser

result = chain.invoke({'question': "what is the product about talking?  ",'text':doc[0].page_content})

print(result)
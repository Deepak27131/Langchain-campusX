from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# model = ChatGroq(model_name="llama3-70b-8192", temperature=0.7)
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)


prompt = PromptTemplate (
    template = "Generate 5 interesting fact about {topic}\n",
    input_variable = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "genAI in India"})

print(result)

chain.get_graph().print_ascii()

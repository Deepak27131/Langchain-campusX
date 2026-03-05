from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}\n",
    input_variable = ['topic']
)

prompt2 = PromptTemplate(
    template = "Genrates a 5 point short summary the following text \n {text}\n",
    input_variable = ['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "langchain"})

print(result)

chain.get_graph().print_ascii()



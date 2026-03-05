from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)


prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)



parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke {text}",
    input_variables=["text"]
)

chain = RunnableSequence(prompt1 , model ,parser, prompt2,model , parser)

print(chain.invoke({'topic' : 'Langchain'}))
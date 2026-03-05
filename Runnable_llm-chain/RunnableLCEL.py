from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnableLambda,RunnablePassthrough,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq( 
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=300   
)

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

parser = StrOutputParser()


# Pehle wala tarika (verbose)
chain = RunnableSequence(prompt1, model, parser)

# LCEL tarika (clean ✅)
chain = prompt1 | model | parser

# Use karo
result = chain.invoke({"topic": "AI"})
print(result)
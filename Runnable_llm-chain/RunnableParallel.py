from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq( 
    model="llama-3.3-70b-versatile",
    temperature=0.7,            
)

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic} ',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate a Linden post about {topic} ',
    input_variables=['topic']
)

parser = StrOutputParser()
parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1,model,parser),
    'linkden' : RunnableSequence(prompt2, model , parser)
})

result = parallel_chain.invoke({'topic' : 'AI'})
print(result['tweet'])
print(result['linkden'])
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel, RunnableLambda,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq( 
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=300            
)
def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template = 'write joke  about {topic} ',
    input_variables=['topic']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt , model , parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chan = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chan.invoke({'topic','AI'})

final_result = """{} \n word count - {}""".format(result['joke'],result['word_count'])

print(final_result)
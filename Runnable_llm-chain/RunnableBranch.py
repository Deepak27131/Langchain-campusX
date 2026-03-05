
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

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Summarize the following text:\n{text}",
    input_variables=["text"]
)

# Report generation chain
report_chain = RunnableSequence(prompt1, model, parser)

# Branch chain
branch_chain = RunnableBranch(
    # Condition 1: Agar 500 words se zyada hai → summarize karo
    (
        lambda x: len(x.split()) > 500,
        RunnableSequence(prompt2, model, parser)  # Summarize
    ),
    # Default (else): As-is print karo
    RunnablePassthrough()
)

# Final chain
final_chain = RunnableSequence(report_chain, branch_chain)
result = final_chain.invoke({"topic": "Russia vs Ukraine"})
print(result)
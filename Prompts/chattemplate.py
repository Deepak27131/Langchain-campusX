from langchain_core.prompts import ChatPromptTemplate

Chat_template = ChatPromptTemplate([
    ('system','You are helpful {domain} experts'),
    ('human','Explain in the simple terms waht is {topic} ')
])

prompt = Chat_template.invoke(
    {'domain':'AI','topic':'LLM'}
)

print(prompt)
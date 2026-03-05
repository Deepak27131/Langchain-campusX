from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, how are you?")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))
print(messages)

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# template with multiple vvariable 

template = """Date :{date}
user: {user_name}
task: {task}

please complet the following  : {request}
"""

prompt = PromptTemplate(
    input_variable = ['user_name', 'task', 'request'],
    template = template
)

formatted = prompt.format(
    user_name = 'Aman',
    task = 'write a email',
    request = 'write a email to Aman',
    date = datetime.now().strftime('%Y-%m-%d')
)

model = ChatGroq(model_name='llama-3.3-70b-versatile', temperature=0.9)

result = model.invoke(formatted)

print(result.content)
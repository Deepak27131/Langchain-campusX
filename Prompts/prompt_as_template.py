from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


prompt = PromptTemplate(
    template = 'you are he helpful asiistance that transalet {input_language} to {output_language} transalation\n {text}',
    input_variables = ['input_language', 'output_language', 'text']
)

formate_prompt = prompt.format(
    input_language = 'english',
    output_language = 'hindi',
    text = 'Hello, how are you?'
)

model = ChatGroq(model_name='llama-3.3-70b-versatile', temperature=0.7)

result = model.invoke(formate_prompt)

print(result.content)
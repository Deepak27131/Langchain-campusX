from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define your data model
class Recipe(BaseModel):
    name: str = Field(description="Name of the recipe")
    prep_time: int = Field(description="Preparation time in minutes")
    servings: int = Field(description="Number of servings")
    ingredients: List[str] = Field(description="List of ingredients")
    difficulty: str = Field(description="Difficulty level: easy, medium, or hard")

# Create parser
parser = PydanticOutputParser(pydantic_object=Recipe)

# Create prompt
prompt = PromptTemplate(
    template="""Extract recipe information from the following text.

{format_instructions}

Text: {recipe_text}""",
    input_variables=["recipe_text"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Use the chain
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    
)
chain = prompt | llm | parser

# Parse recipe
result = chain.invoke({
    "recipe_text": "This easy pasta carbonara takes just 20 minutes to make and serves 4 people. You'll need spaghetti, eggs, bacon, parmesan cheese, and black pepper."
})

print(f"Recipe: {result.name}")
print(f"Time: {result.prep_time} minutes")
print(f"Servings: {result.servings}")
print(f"Ingredients: {', '.join(result.ingredients)}")
print(f"Difficulty: {result.difficulty}")
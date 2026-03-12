
# from langchain.output_parsers.structured import ResponseSchema
# from langchain_core.output_parsers import StructuredOutputParser
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Define the expected structure
# response_schemas = [
#     ResponseSchema(
#         name="name",
#         description="The name of the product"
#     ),
#     ResponseSchema(
#         name="price",
#         description="The price in USD as a number"
#     ),
#     ResponseSchema(
#         name="features",
#         description="A list of key features"
#     ),
#     ResponseSchema(
#         name="in_stock",
#         description="Whether the item is in stock (true/false)"
#     )
# ]

# # Create parser
# output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# # Create prompt
# prompt = PromptTemplate(
#     template="""Extract product information from the following text.
    
# {format_instructions}

# Text: {product_description}""",
#     input_variables=["product_description"],
#     partial_variables={"format_instructions": output_parser.get_format_instructions()}
# )

# # Use the chain
# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )
# chain = prompt | llm | output_parser

# # Example usage
# result = chain.invoke({
#     "product_description": "The new iPhone 15 Pro costs $999 and features a titanium design, A17 Pro chip, and improved camera system. Currently available in stores."
# })

# print(result)
# # {'name': 'iPhone 15 Pro', 'price': 999, 'features': ['titanium design', 'A17 Pro chip', 'improved camera system'], 'in_stock': True}




from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Define the expected structure
class Product(BaseModel):
    name: str = Field(description="The name of the product")
    price: float = Field(description="The price in USD as a number")
    features: list[str] = Field(description="A list of key features")
    in_stock: bool = Field(description="Whether the item is in stock")

# Create parser
output_parser = JsonOutputParser(pydantic_object=Product)

# Create prompt
prompt = PromptTemplate(
    template="""
Extract product information from the following text.

{format_instructions}

Text: {product_description}
""",
    input_variables=["product_description"],
    partial_variables={
        "format_instructions": output_parser.get_format_instructions()
    }
)

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

# Chain
chain = prompt | llm | output_parser

# Example usage
result = chain.invoke({
    "product_description": "The new iPhone 15 Pro costs $999 and features a titanium design, A17 Pro chip, and improved camera system. Currently available in stores."
})

print(result)
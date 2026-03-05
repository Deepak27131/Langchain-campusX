from pydantic import BaseModel,EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str
    cgpa:float = Field(gt=0,lt=10,description="CGPA must be between 0 and 10")
    # age: int
    age: Optional[int] = None
    # email:EmailStr
    
new_student = {'age': '20', 'name': 'Alice', 'cgpa': 8.5}

student = Student(**new_student)
print(student)
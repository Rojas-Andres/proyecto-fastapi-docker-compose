from typing import Optional , List
from pydantic import BaseModel

class UserValidate(BaseModel):
    name:str
    email:str
    password:str
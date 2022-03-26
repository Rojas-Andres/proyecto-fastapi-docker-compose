from typing import Optional , List
from pydantic import BaseModel

class UserValidate(BaseModel):
    name:str
    email:str
    password:str

class Geo(BaseModel):
    lat:str
    lng:str 

class Address(BaseModel):
    geo:Geo
    city:str
    suite:str
    street:str
    zipcode:str

class Company(BaseModel):
    bs:str
    name:str
    catchPhrase:str

class ShowUser(BaseModel):
    name:str
    username:str
    email:str
    address:Address
    phone:str
    website:str
    company:Company
    class Config():
        orm_mode = True
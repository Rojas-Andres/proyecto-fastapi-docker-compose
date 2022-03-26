from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository.user import *
from blog.schemas import *
router = APIRouter(
    prefix='/user',
    tags=['Users']
)

# @router.post('/usersApi',response_model=ShowUserCreate)
# def create_users(request:UserValidate,db:Session=Depends(get_db)):
#     return user.create_user(request,db)

@router.get('/{id}',status_code=200,response_model=ShowUser )
def show(id:int, response:Response, db:Session=Depends(get_db)):
    return show_user(id,response,db)
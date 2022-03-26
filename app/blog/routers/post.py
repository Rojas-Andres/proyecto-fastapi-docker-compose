from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository import post
from blog.schemas import *
from typing import List
router = APIRouter(
    prefix='/post',
    tags=['Posts']
)


@router.get('/{id}',response_model=ShowPost )
def show(id:int, response:Response, db:Session=Depends(get_db)):
    return post.show_post(id,db)

@router.get('/{id}/comments',response_model=List[ShowCommentByPost] )
def show_comment_by_post(id:int, response:Response, db:Session=Depends(get_db)):
    return post.show_comment_by_post(id,db)

@router.post('/',response_model=ShowPost )
def create_post(request:PostValidate,db:Session=Depends(get_db)):
    return post.create_post(request,db)

@router.delete('/{id}')
def destroy(id,db:Session=Depends(get_db)):
    return post.delete_post(id,db)
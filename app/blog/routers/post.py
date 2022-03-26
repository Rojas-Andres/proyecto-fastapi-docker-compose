from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository.post import *
from blog.schemas import *

router = APIRouter(
    prefix='/post',
    tags=['Posts']
)


@router.get('/{id}',response_model=ShowPost )
def show(id:int, response:Response, db:Session=Depends(get_db)):
    return show_post(id,db)
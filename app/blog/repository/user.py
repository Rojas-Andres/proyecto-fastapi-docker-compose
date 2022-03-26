from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status

def show_user(id,db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el usuario con el id {id} por favor vuelva a crear los usuarios')
    return user
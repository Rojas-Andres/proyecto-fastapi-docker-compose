from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status

def show_post(id,db:Session):
    ''' 
        Esta funcion devuelve el post mediante al id
    ''' 
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el post con el id {id} por favor vuelva a crear los post')
    return post
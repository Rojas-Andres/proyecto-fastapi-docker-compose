from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status

def show_album(id,db:Session):
    album = db.query(Album).filter(Album.id == id).first()
    if not album:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el album con el id {id} por favor vuelva a crear los album')
    return album
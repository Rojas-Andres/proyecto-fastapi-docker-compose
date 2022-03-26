from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status

def create_user(user,db:Session):
    ''' 
    Esta funcion primero crea los usuarios
    '''
    new_user = User(id = user["id"],name=user["name"],username=user["username"],email=user["email"],address=user["address"],phone=user["phone"],website=user["website"],company=user["company"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

def delete_all_users(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla users
    '''
    db.query(User).delete()
    db.commit()

def create_todo(todo,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla todo
    ''' 

    ### Validar que el usuario este creado y si no devolver que se debe de crear el usuario con el id tal -> 
    new_todo = Todo(id = todo["id"],title=todo["title"],completed=todo["completed"],userId=todo["userId"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
def delete_all_todos(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla todos
    '''
    db.query(Todo).delete()
    db.commit()

def create_album(album,db:Session):
    ''' 
        Esta funcion crea todos los albums
    '''
    new_album = Album(id = album["id"],title=album["title"],userId=album["userId"])
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
def delete_all_albums(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla albums
    '''
    db.query(Album).delete()
    db.commit()

def create_photos(photo,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla photo
    '''
    new_photo = Photo(id = photo["id"],title=photo["title"],url=photo["url"],albumId=photo["albumId"])
    db.add(new_photo)
    db.commit()
    db.refresh(new_todo)

def delete_all_photos(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla photos
    ''' 
    db.query(Photo).delete()
    db.commit()
from fastapi import APIRouter,Depends,Response,HTTPException,status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository.jsonPlaceHolder import *

router = APIRouter(
    prefix='/jsonPlaceHolder',
    tags=['PlaceHolder Api']
)

@router.post('/crea_users')
def create_users(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/users 
        y llenar la tabla de postgres users
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    delete_all_users(db)
    for user in r.json():
        create_user(user,db)
    return {"respuesta":"Usuarios creados satisfactoriamente!"}

@router.post('/crea_todos')
def create_todos(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/todos
        y llenar la tabla de postgres todos
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    delete_all_todos(db)
    for todo in r.json():
        create_todo(todo,db)
    return {"respuesta":"Todos creados satisfactoriamente!"}
@router.post('/crea_albums')
def create_albums(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/albums
        y llenar la tabla de postgres albums
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/albums')
    delete_all_albums(db)
    for album in r.json():
        create_album(album,db)
    return {"respuesta":"Albumns creados satisfactoriamente!"}

@router.post('/crea_fotos')
def create_fotos(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/photos
        y llenar la tabla de postgres photos
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/photos')
    delete_all_photos(db)
    for photo in r.json():
        create_photos(photo,db)
    return {"respuesta":"Photos creados satisfactoriamente!"}

@router.post('/crea_post')
def create_posts(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/posts
        y llenar la tabla de postgres post
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    delete_all_post(db)
    for post in r.json():
        create_post(post,db)
    return {"respuesta":"Post creados satisfactoriamente!"}

@router.post('/crea_comentarios')
def create_comments(db:Session=Depends(get_db)):
    ''' 
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/comments
        y llenar la tabla de postgres comments
    ''' 
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    delete_all_comments(db)
    for comment in r.json():
        create_comment(comment,db)
    return {"respuesta":"Comments creados satisfactoriamente!"}

# @router.get('/{id}',status_code=200 , response_model=ShowUser)
# def show(id:int, response:Response, db:Session=Depends(get_db)):
#     return user.show_user(id,response,db)
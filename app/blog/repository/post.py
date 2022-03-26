from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status
from blog.repository.user import show_user
from blog.database import engine
def show_post(id,db:Session):
    ''' 
        Esta funcion devuelve el post mediante al id
    ''' 
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el post con el id {id} por favor vuelva a crear los post')
    return post

def create_post(request,db:Session):
    ''' 
        Esta funcion crea un post 
    ''' 
    show_user(request.userId,db)
    new_post = Post(title=request.title,body=request.body,userId=request.userId)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
def show_comment_by_post(id:int,db:Session):
    ''' 
        Esta funcion devuelve todos los comentarios de un post
    ''' 
    show_post(id,db)
    comments_by_post = db.query(Comment).filter(Comment.postId == id ).all()
    if len(comments_by_post)==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'El post {id} aun no tiene comentarios') 
    return comments_by_post 
def delete_post(id:int,db:Session):
    ''' 
        Esta funcion elimina un post
    '''
    post = db.query(Post).filter(Post.id == id )
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No existe el post con el id {id} por lo tanto no se elimino')
    post.delete(synchronize_session=False)
    db.commit()
    return {'Respuesta':f"{id} eliminado con exito!"} 
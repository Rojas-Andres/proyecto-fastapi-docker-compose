from fastapi import FastAPI
from blog.routers import jsonPlaceHolder,user,album,post,comments

app = FastAPI()
app.include_router(jsonPlaceHolder.router)
app.include_router(user.router)
app.include_router(album.router)
app.include_router(post.router)
app.include_router(comments.router)
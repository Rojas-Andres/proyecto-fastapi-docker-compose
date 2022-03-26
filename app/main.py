from fastapi import FastAPI
from blog.routers import jsonPlaceHolder,user,album,post
app = FastAPI()
# app.include_router(authentication.router)
# app.include_router(blog.router)
# app.include_router(user.router)
app.include_router(jsonPlaceHolder.router)
app.include_router(user.router)
app.include_router(album.router)
app.include_router(post.router)
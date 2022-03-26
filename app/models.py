from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    address = Column(JSONB)
    phone = Column(String)
    website = Column(String)
    company = Column(JSONB)
    todos = relationship('Todo',back_populates='creator')
    album = relationship('Album',back_populates='creator_album')
class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(Boolean)
    userId = Column(Integer,ForeignKey('users.id'))
    creator = relationship('User',back_populates='todos')
class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    userId = Column(Integer,ForeignKey('users.id'))
    creator_album = relationship('User',back_populates='album')
    photo = relationship('Photo',back_populates='creator_photo')
class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    completed = Column(Boolean)
    albumId = Column(Integer,ForeignKey('album.id'))
    creator_photo = relationship('Album',back_populates='photo')

# class Ppr(Base):
#     __tablename__ = 'ppr'
#     id = Column(Integer,primary_key=True,index=True)
#     name = Column(String)
# pprs = [
#     Ppr(name="ada "),
#     Ppr(name="adas "),
    
# ]
# # session_maker = sessionmaker(bind=create_engine('postgresql://postgres:postgres@localhost:5435/fastapi'))

# # def crear():
# #     with session_maker() as session:
# #         for u in pprs:
# #             session.add(u)
# #         session.commit()
# # crear()
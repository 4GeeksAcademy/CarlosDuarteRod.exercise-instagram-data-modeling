import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
id = Column(Integer, primary_key=False)
username = Column(String(250), nullable = False)
firstname = Column(String(250), nullable = False)
lasttname = Column(String(250), nullable = True)
email = Column(String(300), nullable = False)


class Followers(Base):
     __tablename__ = 'followers'
User_from_id = Column(Integer, ForeignKey('user.id'))
User_to_id = Column(Integer, ForeignKey("user.id") , nullable = False)
user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
id = Column(Integer, primary_key=False)
title = Column(String(250), nullable = False)
user_id = Column(Integer,ForeignKey('user.id'), nullable = False)
user = relationship(User)
    

class Comment(Base):
     __tablename__ = 'comment'
id = Column(Integer, primary_key=False)
comment_text = Column(String(600), nullable = False)
author_id = Column(Integer,ForeignKey('user.id'), nullable = False)
post_id = Column(Integer, ForeignKey('post.user_id'), nullable = False)
user = relationship(User)
post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key = False)
    type = Column(enumerate, nullable = False)
    url = Column(String, nullable = False)
    post_id = Column(Integer,ForeignKey('post.id'), nullable = False)
    post = relationship(Post)
   
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
    try:
        result = render_er(Base, 'diagram.png')
        print("Success! Check the diagram.png file")
    except Exception as e:
        print("There was a problem genering the diagram")
        raise e

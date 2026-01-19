"""
User
id
phone_number
password
email
username
name
surname
city
date_of_birth
reg_date


UserPost
id
reg_date
main_text
uid

PostPhoto
id
photo_path
pid


Comment
id
text
uid
pid
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    phone_number = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    surname = Column(String)
    city = Column(String)
    date_of_birth = Column(String)
    reg_date = Column(DateTime, default=datetime.now())


class UserPost(Base):
    __tablename__ = "userposts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    reg_date = Column(DateTime, default=datetime.now())
    main_text = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"))

    user_fk = relationship("User", lazy="subquery")

class PostPhoto(Base):
    __tablename__ = "photos"
    id = Column(Integer, autoincrement=True, primary_key=True)
    photo_path = Column(String, nullable=False)
    pid = Column(Integer, ForeignKey("userposts.id"))

    post_fk = relationship("UserPost", lazy="subquery")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, autoincrement=True, primary_key=True)
    text = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey("users.id"))
    pid = Column(Integer, ForeignKey("userposts.id"))

    user_fk = relationship("User", lazy="subquery")
    post_fk = relationship("UserPost", lazy="subquery")










from sqlalchemy import Column,Integer,String,Text,ForeignKey
from db import Base,engine
import pymysql
pymysql.install_as_MySQLdb()

class User(Base):
    __tablename__ ="users"

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(255),unique=True,index=True,nullable=False)
    password=Column(String(255),nullable=False)

class Report(Base):
    __tablename__="reports"

    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    resume_text=Column(Text)
    result=Column(Text)

Base.metadata.create_all(bind=engine)    
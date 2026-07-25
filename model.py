from config import Base
from sqlalchemy import Column,Integer,String,Boolean,BigInteger

class Users(Base):
    __tablename__ ="users" #special variable

    id =Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    mobile=Column(BigInteger)
    password=Column(String)
    status=Column(Boolean,default=True)
from fastapi import FastAPI,Depends
from schema import NewUser, UserList
from sqlalchemy.orm import Session 
from db import get_db_connection
from config import engine, Base
from model import Users
app= FastAPI()


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Server Starts Running"}


@app.post("/add-user",response_model=UserList)
def add_user(user:NewUser, db:Session = Depends(get_db_connection)): 
   db_user = Users(
       name=user.name,
       email=user.email,
       mobile=user.mobile,
       password=user.password
   )

   db.add(db_user)
   db.commit()
   db.refresh(db_user)
   return db_user


@app.get("/get_all_users",response_model=list[UserList])
def get_all_users(db:Session=Depends(get_db_connection)):
    return db.query(Users).all()


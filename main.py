from fastapi import FastAPI,Depends
from schema import NewUser, UserList,LoginRequest
from sqlalchemy.orm import Session 
from db import get_db_connection
from config import engine, Base
from model import Users
from password import hash_password,verify_hash
app= FastAPI()

#It creates the table automatically when table is not found in db
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Server Starts Running"}


@app.post("/add-user",response_model=UserList)
def add_user(user:NewUser, db:Session = Depends(get_db_connection)): #Session --> Interface gives auto suggestion of query methods

   hash_pwd= hash_password(user.password)
   db_user = Users(
       name=user.name,
       email=user.email,
       mobile=user.mobile,
       password=hash_pwd
   )

   db.add(db_user)
   db.commit()
   db.refresh(db_user)
   return db_user


@app.get("/get_all_users",response_model=list[UserList])
def get_all_users(db:Session=Depends(get_db_connection)):
    return db.query(Users).all()

@app.post("/login")
def login(user_info:LoginRequest,db:Session=Depends(get_db_connection)):
    register_info = db.query(Users).filter(Users.email == user_info.email).first()
    hashed_password = register_info.password
    try:
        verified = verify_hash(user_info.password,hashed_password,)
        if verified:
            return {'message':'logged In Successfully'}
        return {'message':'invalid Login'}
    except Exception:
        print("exception while verify", Exception)






from pydantic import BaseModel

#for new user post payload
class NewUser(BaseModel):
    name:str
    email:str
    mobile:int
    password:str


#get api list data validation
class UserList(BaseModel):
    id:int
    name:str
    email:str
    status:bool

    #convert sqlalchecmy model in to reponse based JSON 
    class config():
        from_attributes =True

class LoginRequest(BaseModel):
    password:str
    email:str


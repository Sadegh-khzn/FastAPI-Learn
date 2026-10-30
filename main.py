from fastapi import FastAPI , status , HTTPException 
from schema import UserRequest , userResponse ,userOutput , UserPathRequest
from typing import List
from services.user import User_service

app = FastAPI()
user_service = User_service()


@app.post("/user" , response_model=userResponse , status_code=status.HTTP_201_CREATED)
def create_user(user:UserRequest):
    new_user = user_service.create_user(user)
    return {"message" : "user_created" , "user" : new_user}


@app.get("/user" , response_model=List[userOutput])
def get_users():
    return user_service.get_users()


@app.get("/user/{user_id}",response_model=userOutput)
def get_user(user_id:int):
    return user_service.get_user(user_id=user_id)


@app.put("/user/{user_id}",response_model=userResponse)
def update_user(user_id:int,user:UserRequest):
    existing_user =user_service.update_user(user_id=user_id,user=user)
    return {"message":"user updated","user":existing_user}


@app.patch("/user/{user_id}",response_model=userResponse)
def path_user(user_id : int , user:UserPathRequest):
    existing_user = user_service.patch_user(user_id=user_id,user=user)
    return {"message" :"user path updated" , "user" : existing_user}


@app.delete("/user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    user_service.delete_user(user_id=user_id)
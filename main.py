from fastapi import FastAPI , status , Depends
from schema import UserRequest , userResponse ,userOutput , UserPathRequest
from typing import List
from services.user import User_service
from contextlib import asynccontextmanager
from dependencies import get_user_servies





@asynccontextmanager
async def lifespan(app :FastAPI):
    app.state.counter = 0
    print("Server started")
    yield
    print("Server Shutdown")

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    app.state.counter += 1
    return {"hello":"world","counter":app.state.counter}

@app.post("/user" , response_model=userResponse , status_code=status.HTTP_201_CREATED)
def create_user(
    user:UserRequest,
    user_service : User_service = Depends(get_user_servies) ):
    new_user = user_service.create_user(user)
    return {"message" : "user_created" , "user" : new_user}


@app.get("/user" , response_model=List[userOutput])
def get_users(user_service : User_service = Depends(get_user_servies)):
    return user_service.get_users()


@app.get("/user/{user_id}",response_model=userOutput)
def get_user(user_id:int , user_service:User_service=Depends(get_user_servies)):
    return user_service.get_user(user_id=user_id)


@app.put("/user/{user_id}",response_model=userResponse)
def update_user(user_id:int,user:UserRequest , user_service: User_service = Depends(get_user_servies)):
    existing_user =user_service.update_user(user_id=user_id,user=user)
    return {"message":"user updated","user":existing_user}


@app.patch("/user/{user_id}",response_model=userResponse)
def path_user(user_id : int , user:UserPathRequest , user_service : User_service=Depends(get_user_servies)):
    existing_user = user_service.patch_user(user_id=user_id,user=user)
    return {"message" :"user path updated" , "user" : existing_user}


@app.delete("/user/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int , user_service : User_service = Depends(get_user_servies)):
    user_service.delete_user(user_id=user_id)
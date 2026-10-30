from fastapi import FastAPI ,Depends , HTTPException ,status
from typing import Optional

app = FastAPI()

def gereeting():
    return "hello world"
def get_query_params(page:Optional[int] = None):
    return {"page":page}
def get_path_params(user_id:int):
    return {"user_id":user_id}
def get_token(token:int):
    if token != 1234:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid token")
    return {"token":token}

@app.get("/{user_id:int}")
def read_root(
    message : str = Depends(gereeting),
    query_param:dict = Depends(get_query_params),
    path_param:dict = Depends(get_path_params),
    token:dict=Depends(get_token)):
    return {"message" : message , "query params":query_param , "path params":path_param, "token" : token}
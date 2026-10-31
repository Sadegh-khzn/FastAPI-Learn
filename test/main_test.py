from fastapi import FastAPI ,Depends
from depends_test import gereeting, get_path_params, get_query_params, get_token

app = FastAPI()

@app.get("/{user_id:int}")
def read_root(
    message : str = Depends(gereeting),
    query_param:dict = Depends(get_query_params),
    path_param:dict = Depends(get_path_params),
    token:dict=Depends(get_token)):
    
    return {"message" : message ,
            "query params":query_param ,
            "path params":path_param,
            "token" : token}
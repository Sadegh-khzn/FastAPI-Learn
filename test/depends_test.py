from typing import Optional
from exceptions_test import InvalidTokenExeption
from fastapi.security import APIKeyHeader
from fastapi import Depends
api_key_header_token = APIKeyHeader(name="Token",auto_error=True)

def gereeting():
    return "hello world"

def get_query_params(page:Optional[int] = None):
    return {"page":page}

def get_path_params(user_id:int):
    return {"user_id":user_id}

def get_token(token:int =Depends(api_key_header_token)):
    if token != "1234":
       raise InvalidTokenExeption()
    return {"token":token}
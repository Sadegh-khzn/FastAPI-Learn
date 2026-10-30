from schema import userOutput
from fastapi import HTTPException , status
from exceptioans import UserNotFoundExceptian ,EmailAlreadyExistException
def get_usr_or_404(users :userOutput , user_id:int):
    exsiting_user = next(u for u in users if u.id == user_id)
    if not exsiting_user:
        raise UserNotFoundExceptian()

def email_already_exist(users:list[userOutput],email:str):
    if any(e.email == email for e in users ):
        raise EmailAlreadyExistException()

def email_already_exist_update(users:list[userOutput],email:str,existing_user:userOutput):
    if any(u.email == email and u.email != existing_user.email for u in users):
        raise EmailAlreadyExistException()
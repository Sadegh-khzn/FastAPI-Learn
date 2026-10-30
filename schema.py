from pydantic import BaseModel , Field ,EmailStr
from typing import Optional

class UserRequest(BaseModel):
    name : str = Field(...,min_length=5 , max_length= 50, description="the name of the user")
    age : int = Field(...,ge=1 , le= 120, description="the age of the user")
    email : EmailStr = Field (...,format="email" , description="the email of user")
    password : str = Field(...,min_length=8 , max_length= 20 , description="the password of user")
 
class UserPathRequest(BaseModel):
    name : Optional[str] = Field(None,min_length=5 , max_length= 50, description="the name of the user")
    age :Optional[int] = Field(None,ge=1 , le= 120, description="the age of the user")
    email : Optional[EmailStr] = Field (None,format="email" , description="the email of user")
    password : Optional[str] = Field(None,min_length=8 , max_length= 20 , description="the password of user")

class userOutput(BaseModel):
    id : int = Field(description="the id of the user")
    name : str = Field(min_length=5 , max_length= 50, description="the name of the user")
    age : int = Field(ge=1 , le= 120, description="the age of the user")
    email : EmailStr = Field (format="email" , description="the email of user")

class userResponse(BaseModel):
    message : str = Field(description="the message of the response")
    user : userOutput = Field(description="output of user")
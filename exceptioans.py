from fastapi import HTTPException , status

class UserNotFoundExceptian(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

class EmailAlreadyExistException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Email address already exist")

from fastapi import status
from fastapi import HTTPException

class InvalidTokenExeption(HTTPException):
    def __init__(self):
        super().__init__(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="invalid token"
        )

from exceptioans import UserNotFoundExceptian ,EmailAlreadyExistException
from schema import userOutput,UserRequest,UserPathRequest


class User_service:

    def __init__(self):
        self.users = []

    def _get_user_or_404(self,user_id:int):
        exsiting_user = next((u for u in self.users if u.id == user_id),None)
        if not exsiting_user:
            raise UserNotFoundExceptian()
        return exsiting_user

    def _email_already_exist(self,email:str):
        if any(e.email == email for e in self.users ):
            raise EmailAlreadyExistException()

    def _email_already_exist_update(self,email:str,existing_user:userOutput):
        if any(u.email == email and u.email != existing_user.email for u in self.users):
            raise EmailAlreadyExistException()
        
    def create_user(self,user:UserRequest):
        self.email_already_exist(user.email)
        new_user = userOutput(
            id=len(self.users),
            **user.model_dump()
        )
        self.users.append(new_user)
        return new_user

    def get_user(self,user_id:int):
        return self._get_user_or_404(user_id=user_id)

    def get_users(self):
        return self.users

    def update_user(self, user_id:int, user:UserPathRequest):
        existing_user = self._get_user_or_404(user_id)
        self._email_already_exist_update(email=user.email,existing_user=existing_user)
        existing_user.update(user.model_dump())
        return existing_user

    def patch_user(self, user_id:int , user:UserPathRequest ):
        existing_user = self._get_user_or_404(user_id)
        self._email_already_exist_update(email=user.email,existing_user=existing_user)
        existing_user.update(user.model_dump())
        return existing_user
    def delete_user(self,user_id:int ):
        self.users.remove(self._get_user_or_404(user_id))
from typing import Union
from deta import Deta
from app.user.dto import CreateUserDTO
from database.models.user import User
from utils import hash_pasword, save_file
from uuid import uuid4


class UserService:
    
    _deta: Deta
    
    def __init__(self,deta: Deta) -> None:
        self._deta = deta

    async def get_use_by_email(self,email: str) -> Union[User,None]:
        users = await User.query(User.email == email)
        if len(users) > 0:
            return users[0]
        return None

    async def create_user(self,data: CreateUserDTO):
        filename = await save_file(self._deta,data.image,"images",True)
        user = User(**data.dict(exclude={"password","image",}),
                    image=filename,
                    password=hash_pasword(data.password), key=str(uuid4()))
        await user.save()
        return user

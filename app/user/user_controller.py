from typing import Any, Union
from starlite import Controller, Provide, Request, get, post, Body, RequestEncodingType
from app.user.dto import CreateUserDTO
from app.user.user_service import UserService
from database.models import User


class UserController(Controller):
    path = "/users"
    tags = ["Users"]
    security = [{"BearerToken": []}]

    dependencies = {"service": Provide(UserService)}

    @get('/me')
    async def me(self, request: Request[Any, Any]) -> Union[ User,None]:
        return await User.get(request.user.key)

    @get()
    async def list(self) -> list[User]:
        return await User.get_all()

    @post()
    async def create(self, service:  UserService, data: CreateUserDTO = Body(media_type=RequestEncodingType.MULTI_PART)) -> User:
        return await service.create_user(data)

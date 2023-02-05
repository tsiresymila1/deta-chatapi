from typing import Any, Union
import bcrypt
from starlite import ASGIConnection, Body, Controller, Provide, Request, RequestEncodingType, Response, Router, post, ValidationException
from starlite.contrib.jwt import Token, JWTAuth
from app.auth.dto import LoginDto
from app.user.dto import CreateUserDTO
from app.user.user_service import UserService
from database.models import User
from app.auth.middleware import jwt_auth
import os
from datetime import timedelta




class AuthController(Controller):
    tags = ["Auth"]
    path = "/auth"

    dependencies = {"service": Provide(UserService)}

    @staticmethod
    def get_auth() -> JWTAuth[User]:
        return AuthController.auth

    def __init__(self, owner: "Router") -> None:
        super().__init__(owner)
        self.auth = jwt_auth

    @post("/login")
    async def login(self, service: UserService, request: "Request[Any, Any]", data: LoginDto = Body(media_type=RequestEncodingType.JSON)) -> Response[User]:
        user: User | None = await service.get_use_by_email(data.email)
        if user:
            p = user.password.encode('utf8')
            try:
                is_verify_password = bcrypt.checkpw(
                    data.password.encode('utf8'), p)
                if is_verify_password:
                    await request.cache.set(str(user.key), user.dict())
                    response = self.auth.login(
                        token_expiration=timedelta(days=1),
                        identifier=str(user.key), response_body=user)
                    return response
                else:
                    raise ValidationException(detail="Password incorrect")
            except Exception:
                raise ValidationException(detail="Password incorrect")
        else:
            raise ValidationException(detail="User not found")

    @post("/register")
    async def register(self, service: UserService, request: "Request[Any, Any]",
                       data: CreateUserDTO = Body(media_type=RequestEncodingType.MULTI_PART)) -> Response[User]:
        user: User = await service.create_user(data)
        await request.cache.set(str(user.key), user.dict())
        response = self.auth.login(
            token_expiration=timedelta(days=1),
            identifier=str(user.key), response_body=user)
        return response

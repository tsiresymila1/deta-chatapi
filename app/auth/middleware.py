from starlite import ASGIConnection, AbstractAuthenticationMiddleware, AuthenticationResult, DefineMiddleware, NotAuthorizedException
from typing import Any, Union
from starlite.contrib.jwt import Token
from database.models.user import User
from starlite.contrib.jwt import Token, JWTAuth
import os


class JWTAuthenticationMiddleware(AbstractAuthenticationMiddleware):
    async def authenticate_request(self, connection: ASGIConnection) -> AuthenticationResult:
        auth_header = connection.headers.get('Authorization')
        if not auth_header:
            raise NotAuthorizedException()
        token: Token = Token.decode(
            encoded_token=auth_header.replace('Bearer ', ''),
            secret=os.getenv("JWT_SECRET", "abcd123"),
            algorithm="HS256"
        )
        cached_value = await connection.cache.get(token.sub)
        if cached_value:
            return AuthenticationResult(user=User(**cached_value), auth=token)
        raise NotAuthorizedException()


jwt_auth2 = DefineMiddleware(JWTAuthenticationMiddleware, exclude=[
    "/api/auth/login", "/api/auth/register"])


async def retrieve_user_handler(token: Token, connection: ASGIConnection) -> Union[User, None]:
    cached_value = await connection.cache.get(token.sub)
    if cached_value:
        return User(**cached_value)
    return None

jwt_auth = JWTAuth[User](
    retrieve_user_handler=retrieve_user_handler,
    token_secret=os.getenv('JWT_SECRET', 'adbcdabdcd'),
    exclude=["/api/auth/login", "/api/auth/register"],
)

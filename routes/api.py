from starlite import Router
from app.auth.auth_controller import AuthController
from app.auth.middleware import jwt_auth, jwt_auth2

from app.user import UserController
from app.chat import ChatController

api_router = Router(
    path="/api", middleware=[jwt_auth.middleware], route_handlers=[AuthController, UserController, ChatController])

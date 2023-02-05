

from app.middleware import CORSMiddleware
from plugins import ODetaMPlugin
from modules.socketio import SocketManager
from starlite.types import ASGIApp, Scope, Receive, Send
from ressources import Vite
from routes import api_router, web_router
from app.auth.middleware import jwt_auth
import os
from starlite.response import RedirectResponse
from starlite.contrib.jinja import JinjaTemplateEngine
from starlite import  HttpMethod, OpenAPIConfig, Request, Response, Starlite, StaticFilesConfig, TemplateConfig
from starlite.status_codes import HTTP_405_METHOD_NOT_ALLOWED
from starlite.exceptions import MethodNotAllowedException
from typing import Any
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

template_config = TemplateConfig(
    directory=Path(os.getcwd(), "ressources", "views"),
    engine=JinjaTemplateEngine,
)
template_config.engine_instance.engine.globals['vite'] = Vite.vite


def handle_method_not_allowed(request: Request, exc: MethodNotAllowedException) -> Response:
    if request.method == HttpMethod.GET:
        return RedirectResponse(url="/")
    return Response(content={"detail": exc.detail, "status_code": exc.status_code}, status_code=exc.status_code)


def middleware_factory(app: ASGIApp) -> ASGIApp:
    async def header_transoform_middleware(scope: Scope, receive: Receive, send: Send) -> None:
        scope['_headers'] = tuple(scope["headers"])
        await app(scope, receive, send)

    return header_transoform_middleware


starlite_app = Starlite(
    template_config=template_config,
    allowed_hosts=['*'],
    plugins=[ODetaMPlugin()],
    debug=False,
    exception_handlers={
        HTTP_405_METHOD_NOT_ALLOWED: handle_method_not_allowed
    },
    route_handlers=[api_router, web_router],
    openapi_config=OpenAPIConfig(
        title="CHAT API",
        version="1.0.0",
        components=[jwt_auth.openapi_components],
        security=[jwt_auth.security_requirement]
    ),
    middleware=[middleware_factory, CORSMiddleware],
    static_files_config=[
        StaticFilesConfig(
            path="/static",
            directories=[Path(os.getcwd(), "public", "static")]
        ),
    ],
)

io = SocketManager(app=starlite_app)


@io.on("connect")
def connect(sid: Any, environ: Any):
    print("Client connected : ,", sid, environ)


@io.on('message')
async def message(sid: Any, data: Any):
    print("message : ", sid, data)
    await io.emit('message', {"response": []})


@io.on("disconnect")
def disconnect(sid: Any):
    print("Client disconnect : ", sid)


app = io.get_asgi_app()

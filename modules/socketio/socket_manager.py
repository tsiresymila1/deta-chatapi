from typing import Any, TypeVar, Union
from starlite import Starlite, Provide
from starlite.types import Scope, Receive, Send
import socketio


T = TypeVar("T")


class SocketManager:
    _app: socketio.ASGIApp
    _sio: socketio.AsyncServer
    _dependencies: dict[str, Any] = {}
    _starlite: Starlite

    def __init__(
            self,
            app: Starlite,
            socketio_path: str = "socket.io",
            cors_allowed_origins: Union[str, list] = '*',
            namespace: str = "/",
            async_mode: str = "asgi",
            **kwargs
    ):
        self._sio = socketio.AsyncServer(
            logger=True,
            engineio_logger=True,
            async_mode=async_mode, cors_allowed_origins=cors_allowed_origins, namespaces=namespace, **kwargs)

        app.dependencies.update({"sio": Provide(lambda: self)})
        if "deta" in app.dependencies.keys():
            deta = app.dependencies.get("deta")
            self._dependencies["deta"] = deta.dependency.value

        self._app = socketio.ASGIApp(
            socketio_path=socketio_path,
            socketio_server=self._sio, other_asgi_app=app)
        self._starlite = app

    def get_asgi_app(self) -> socketio.ASGIApp:
        return self._app

    def is_asyncio_based(self) -> bool:
        return True

    async def socket_io_handler(self, scope: Scope, receive: Receive, send: Send) -> None:
        await self._app(scope=scope, receive=receive, send=send)

    def load_dependancy(self, key: str) -> T:
        if key in self._dependencies.keys() :
            return self._dependencies[key]()
        return None

    @property
    def on(self):
        return self._sio.on

    @property
    def attach(self):
        return self._sio.attach

    @property
    def emit(self):
        return self._sio.emit

    @property
    def send(self):
        return self._sio.send

    @property
    def call(self):
        return self._sio.call

    @property
    def close_room(self):
        return self._sio.close_room

    @property
    def get_session(self):
        return self._sio.get_session

    @property
    def save_session(self):
        return self._sio.save_session

    @property
    def session(self):
        return self._sio.session

    @property
    def disconnect(self):
        return self._sio.disconnect

    @property
    def handle_request(self):
        return self._sio.handle_request

    @property
    def start_background_task(self):
        return self._sio.start_background_task

    @property
    def sleep(self):
        return self._sio.sleep

    @property
    def enter_room(self):
        return self._sio.enter_room

    @property
    def leave_room(self):
        return self._sio.leave_room

    @property
    def event(self):
        return self._sio.event

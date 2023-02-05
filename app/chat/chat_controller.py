from typing import Any, Union
from starlite import Body, Controller, Provide, Request, RequestEncodingType, get, post
from deta import Deta
from app.chat.chat_service import ChatService
from app.chat.dto import ChatDto, MessageDto
from database.models.message import Message


class ChatController(Controller):
    path = "/chat"
    tags = ["Chats"]

    dependencies = {"service": Provide(ChatService)}

    @get()
    async def list_chat(self, request: Request[Any, Any], service: ChatService) -> list[dict[str, Any]]:
        return await service.list_chat(request.user.key)

    @post()
    async def find(self, request: Request[Any, Any], service: ChatService, data: ChatDto) -> dict[str, Any]:
        return await service.find(user_key=request.user.key, keys=data.keys)

    @get('/{key:str}/detail')
    async def detail(self, key: str, request: Request[Any, Any], service: ChatService) -> Union[dict[str, Any], None]:
        return await service.get_detail(user_key=request.user.key, key=key)

    @post('/{key:str}/send')
    async def send(self, key: str, deta: Deta,  request: Request[Any, Any], service: ChatService, data: MessageDto = Body(media_type=RequestEncodingType.MULTI_PART),) -> list[Message]:
        return await service.send_message(deta=deta, user_key=request.user.key, conversation_key=key, data=data)

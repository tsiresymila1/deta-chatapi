from typing import Any, Union

from app.chat.dto import MessageDto
from database.models.conversation import Conversation
from uuid import uuid4
from database.models.message import Message

from deta import Deta
from database.models.user import User
from utils import save_file


class ChatService():

    async def add_participant(self, conv: Conversation) -> dict[str, Any]:

        participants = []
        for key in conv.pacticipants_keys:
            user = await User.get(key)
            if user != None:
                participants.append(user)

        return {
            **conv.dict(),
            "participants": participants,
            "messages": []
        }

    async def list_chat(self, key: str) -> list[dict[str, Any]]:
        conversations = await Conversation.get_all()
        convs = []
        for c in conversations:
            conv = await self.add_participant(conv=c.copy())
            messages = await Message.query(Message.conversation_key == c.key)
            if len(messages) > 0:
                conv = {
                    **conv.copy(),
                    "messages": [messages[0]]
                }
            convs.append(conv)
        return convs

    async def create_chat(self, user_key: str, keys: list[str]) -> dict[str, Any]:
        conversation_key = str(uuid4())
        conversation = Conversation(
            initiator_key=user_key, title="", key=conversation_key, pacticipants_keys=keys)
        await conversation.save()

        return await self.add_participant(conv=conversation)

    async def find(self, user_key: str, keys: list[str]):
        conversations = await Conversation.get_all()
        conv = None
        for c in conversations:
            inter = list(filter(lambda x: x not in c.pacticipants_keys, keys))
            if len(inter) == 0 and len(c.pacticipants_keys) == len(keys):
                conv = await self.add_participant(conv=c.copy())
                messages = await Message.query(Message.conversation_key == c.key)
                # make user as reader
                for k, m in enumerate(messages):
                    if user_key not in m.readers_keys:
                        m.readers_keys.append(user_key)
                        m.save()
                    if k == len(messages) - 1:
                        conv = {
                            **conv,
                            "messages": [m]
                        }

                return conv
        if not conv:
            return self.create_chat(user_key=user_key, keys=keys)
        return conv

    async def get_detail(self, user_key: str, key: str) -> Union[dict[str, Any], None]:
        conversation = await Conversation.get(key)
        if conversation != None:
            conv = await self.add_participant(conv=conversation)
            messages = await Message.query(Message.conversation_key == conversation.key)
            messs = []
            for m in messages:
                if user_key not in m.readers_keys:
                    m.readers_keys.append(user_key)
                    m.save()
                messs.append(m)
            return {
                **conv,
                "messages": messs
            }
        return None

    async def send_message(elf, user_key: str, conversation_key: str, deta: Deta, data: MessageDto ) -> list[Message]:
        messages = []
        if data.content != None:
            _key = str(uuid4())
            message = Message(conversation_key=conversation_key, sender_key=user_key,
                              content=data.content, type="SIMPLE", readers_keys=[user_key], key=_key)
            messages.append(message)
            message.save()
        if data.files != None:
            for file in data.files:
                _key = str(uuid4())
                filename = await save_file(deta=deta, file=file, directory="medias", encrypted=True)
                message = Message(conversation_key=conversation_key, sender_key=user_key,
                                  content=filename, type="MEDIA", readers_keys=[user_key],key=_key)
                messages.append(message)
                message.save()
        return messages

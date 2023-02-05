from odetam.async_model import AsyncDetaModel
from pydantic import BaseConfig

class Message(AsyncDetaModel):
    conversation_key: str
    sender_key: str
    content: str
    type: str
    readers_keys: list[str]

    class Config(BaseConfig):
        table_name = "messages"

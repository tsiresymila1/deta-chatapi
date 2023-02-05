from typing import Optional
from odetam.async_model import AsyncDetaModel
from pydantic import BaseConfig


class Conversation(AsyncDetaModel):
    title: Optional[str]
    initiator_key: str
    pacticipants_keys: list[str]

    class Config(BaseConfig):
        table_name = "conversations"

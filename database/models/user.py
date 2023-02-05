from odetam.async_model import AsyncDetaModel
from pydantic import BaseConfig


class User(AsyncDetaModel):
    username: str
    email: str
    password: str
    image: str

    class Config(BaseConfig):
        table_name = "users"

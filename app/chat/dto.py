from typing import Optional
from pydantic import BaseConfig, BaseModel
from starlite import UploadFile


class ChatDto(BaseModel) :
    keys: list[str]
    
class MessageDto(BaseModel) :
    content:  Optional[str]
    files: Optional[list[UploadFile]]
    
    class Config(BaseConfig) :
        arbitrary_types_allowed = True
    
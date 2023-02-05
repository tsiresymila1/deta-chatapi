from pydantic import BaseModel,BaseConfig

class LoginDto(BaseModel) :
    email: str
    password: str
    
    class Config(BaseConfig):
        arbitrary_types_allowed = True
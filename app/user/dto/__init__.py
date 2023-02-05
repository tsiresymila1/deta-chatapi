from pydantic import BaseConfig, BaseModel,validator
from starlite import UploadFile

class CreateUserDTO(BaseModel) :
    email: str
    username: str
    password: str
    image: UploadFile
    
    # @validator('email')
    # def validate_name(cls,v) :
    #     return v.title()
    
    class Config(BaseConfig):
        arbitrary_types_allowed = True
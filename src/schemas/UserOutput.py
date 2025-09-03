from pydantic import BaseModel, EmailStr

class UserOutput():
    id:str
    email:str
    
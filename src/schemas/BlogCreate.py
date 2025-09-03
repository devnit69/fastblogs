from pydantic import BaseModel, EmailStr
from uuid import uuid4

class BlogCreate(BaseModel):
    content :str
    user_id : str

from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    first_name : str
    last_name : str

class User(UserBase):
    user_id: UUID
    first_name:str
    last_name : str
    date_joined: datetime

    class Config:
        orm_mode = True
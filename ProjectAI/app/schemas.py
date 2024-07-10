from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class MessageCreate(BaseModel):
    content: str
    user_id: int

class Message(BaseModel):
    id: int
    content: str
    user_id: int

    class Config:
        orm_mode = True

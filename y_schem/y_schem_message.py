from datetime import *
from pydantic import BaseModel

class SchemBaseMessage(BaseModel):
    text: str
    id_chat: int
    id_member: int

class SchemMessageCreate(SchemBaseMessage):
    pass

class SchemMessage(SchemBaseMessage):
    id: int
    date: datetime

    class Config:
        orm_mode = True
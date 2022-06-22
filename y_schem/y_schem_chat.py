from pydantic import BaseModel

class SchemBaseChat(BaseModel):
    pass

class SchemChatCreate(BaseChat):
    pass

class SchemChat(BaseChat):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class SchemBaseChat(BaseModel):
    pass

class SchemChatCreate(SchemBaseChat):
    pass

class SchemChat(SchemBaseChat):
    id: int

    class Config:
        orm_mode = True
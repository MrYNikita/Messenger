from pydantic import BaseModel

# схема парных чатов
class SchemBaseChatPair(BaseModel):
    id_user_one: int
    id_user_two: int

class SchemChatPairCreate(SchemBaseChatPair):
    pass

class SchemChatPair(SchemBaseChatPair):
    id: int

    class Config:
        orm_mode = True

# схема групповых чатов
class SchemBaseChatGroup(BaseModel):
    pass

class SchemChatGroupCreate(SchemBaseChatGroup):
    pass

class SchemChatGroup(SchemBaseChatGroup):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class SchemBaseChatMember(BaseModel):
    pass

class SchemChatMemberCreate(SchemBaseChatMember):
    pass

class SchemChatMember(SchemBaseChatMember):
    id: int
    id_chat: int
    id_ChatMember: int

    class Config:
        orm_mode = True
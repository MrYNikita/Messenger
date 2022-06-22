from pydantic import BaseModel

class SchemBaseMember(BaseModel):
    pass

class SchemMemberCreate(SchemBaseMember):
    pass

class SchemMember(SchemBaseMember):
    id: int
    id_chat: int
    id_user: int

    class Config:
        orm_mode = True
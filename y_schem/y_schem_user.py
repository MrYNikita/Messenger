from pydantic import BaseModel

class SchemBaseUser(BaseModel):
    nickname: str

class SchemUserCreate(SchemBaseUser):
    login: str
    password: str

class SchemUser(SchemBaseUser):
    id: int

    class Config:
        orm_mode = True
from pydantic import BaseModel

class SchemBaseUser(BaseModel):
    login: str
    nickname: str

class SchemUserCreate(SchemBaseUser):
    password: str

class SchemUser(SchemBaseUser):

    class Config:
        orm_mode = True
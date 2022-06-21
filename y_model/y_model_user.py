from y_db import *

class ModelUser(db):
    __tablename__ = 'User'
    login = Column(String, primary_key=True)
    nickname = Column(String)
    password = Column(String)

    def __init__(self, login: str, nickname: str, password: str):
        self.login = login
        self.nickname = nickname
        self.password = password
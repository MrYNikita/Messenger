from y_db import *

class ModelUser(db):
    __tablename__ = 'User'
    id = Column(Integer, Sequence('User_id_seq'), primary_key=True)
    login = Column(String)
    nickname = Column(String)
    password = Column(String)

    def __init__(self, login: str, nickname: str, password: str):
        self.login = login
        self.nickname = nickname
        self.password = password
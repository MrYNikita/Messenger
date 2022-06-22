from y_db import *

class ModelMember(db):
    __tablename__ = 'ChatMember'
    id = Column(Integer, Sequence('ChatMember_id_seq'), primary_key=True)
    id_user = Column(Integer)
    id_chat = Column(Integer)

    def __init__(self, id_user: int, id_chat: int):
        self.id_user = id_user
        self.id_chat = id_chat
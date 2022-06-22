from y_db import *

class ModelChat(db):
    __tablename__ = 'Chat'
    id = Column(Integer, Sequence('Chat_id_seq'), primary_key=True)

class ModelChatPair(ModelChat):
    __tablename__ = 'ChatPair'
    id = Column(Integer,ForeignKey('Chat.id'),primary_key=True)
    id_user_one = Column(Integer)
    id_user_two = Column(Integer)

    def __init__(self, id_user_one: int, id_user_two):
        self.id_user_one = id_user_one
        self.id_user_two = id_user_two

class ModelChatGroup(ModelChat):
    __tablename__ = 'ChatGroup'
    id = Column(Integer,ForeignKey('Chat.id'),primary_key=True)
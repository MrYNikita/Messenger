from y_db import *

class ModelChat(db):
    __tablename__ = 'Chat'
    id = Column(Integer, Sequence('Chat_id_seq'), primary_key=True)
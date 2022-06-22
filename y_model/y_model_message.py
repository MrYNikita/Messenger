from datetime import datetime
from y_db import *

class ModelMessage(db):
    __tablename__ = 'Message'
    id = Column(Integer, Sequence('Message_id_seq'), primary_key=True)
    id_chat = Column(Integer)
    id_member = Column(Integer)
    text = Column(String)
    date = Column(DateTime)

    def __init__(self, id_chat: int, id_member: int, text: str):
        self.text = text
        self.date = datetime.now()
        self.id_chat = id_chat
        self.id_member = id_member
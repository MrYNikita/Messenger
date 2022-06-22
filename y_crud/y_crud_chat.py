# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_chat import ModelChat
# импорт схемы
from y_schem.y_schem_chat import SchemChatCreate

def crud_chat_get_by_id(db: Session, id: int):
    return db.query(ModelChat).filter(ModelChat.id == id).first()

def create_chat(db: Session, chat: SchemChatCreate):
    db_chat = ModelChat()
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat
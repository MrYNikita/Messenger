# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_chat import ModelChatPair
# импорт схемы
from y_schem.y_schem_chat import SchemChatPairCreate

def crud_chat_pair_get_by_id(db: Session, id: int):
    return db.query(ModelChatPair).filter(ModelChatPair.id == id).first()

def crud_chat_pair_get_by_users(db: Session, id_user_one: int, id_user_two: int):
    return db.query(ModelChatPair).filter(ModelChatPair.id_user_one == id_user_one, ModelChatPair.id_user_two == id_user_two).first()

def crud_chat_pair_create(db: Session, chat: SchemChatPairCreate):
    db_chat = ModelChatPair(chat.id_user_one,chat.id_user_two)
    db.add(db_chat)
    db.commit()
    db.refresh(db_chat)
    return db_chat
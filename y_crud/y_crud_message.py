# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_message import ModelMessage
# импорт схемы
from y_schem.y_schem_message import SchemMessageCreate

# функция получения сообщения по id
def crud_message_get_by_id(db: Session, id: int):
    return db.query(ModelMessage).filter(ModelMessage.id == id).first()

# функция получения сообщений по id чата
def crud_message_get_by_id(db: Session, id_chat: int):
    return db.query(ModelMessage).filter(ModelMessage.id_chat == id_chat).all()

# функция получения сообщений по id участника
def crud_message_get_by_id(db: Session, id_member: int):
    return db.query(ModelMessage).filter(ModelMessage.id_member == id_member).all()

# функция добавления пользователя по схеме с сохранением в бд
def crud_message_create(db: Session, message: SchemMessageCreate):
    db_message = ModelMessage(text = message.text, id_chat = message.id_chat, id_member = message.id_member)
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message
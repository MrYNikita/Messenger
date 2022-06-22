# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_chat_member import ModelChatMember
# импорт схемы
from y_schem.y_schem_chat_member import SchemChatMemberCreate

# функция получения участника по id
def crud_chat_member_get_by_id(db: Session, id: int):
    return db.query(ModelChatMember).filter(ModelChatMember.id == id).first()

# функция получения участников по id чата
def crud_chat_member_get_by_id(db: Session, id_chat: int):
    return db.query(ModelChatMember).filter(ModelChatMember.id_chat == id_chat).all()

# функция получения участников по id пользователя
def crud_chat_member_get_by_id(db: Session, id_user: int):
    return db.query(ModelChatMember).filter(ModelChatMember.id_user == id_user).all()

# функция получения участника по id пользователя и чата
def crud_chat_member_get_by_id(db: Session, id_user: int, id_chat):
    return db.query(ModelChatMember).filter(ModelChatMember.id_user == id_user, ModelChatMember.id_chat == id_chat).all()

# функция добавления участника по схеме с сохранением в бд
def crud_chat_member_create(db: Session, chatMember: SchemChatMemberCreate):
    db_ChatMember = ModelChatMember(chatMember.user_id,chatMember.chat_id)
    db.add(db_ChatMember)
    db.commit()
    db.refresh(db_ChatMember)
    return db_ChatMember
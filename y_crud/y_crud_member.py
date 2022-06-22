# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_member import ModelMember
# импорт схемы
from y_schem.y_schem_member import SchemMemberCreate

# функция получения участника по id
def crud_member_get_by_id(db: Session, id: int):
    return db.query(ModelMember).filter(ModelMember.id == id).first()

# функция получения участников по id чата
def crud_member_get_by_id_chay(db: Session, id_: int):
    return db.query(ModelMember).filter(ModelMember.id_ == id_).all()

# функция получения участников по id пользователя
def crud_member_get_by_id_user(db: Session, id_user: int):
    return db.query(ModelMember).filter(ModelMember.id_user == id_user).all()

# функция получения участника по id пользователя и чата
def crud_member_get_by_id_user_(db: Session, id_user: int, id_):
    return db.query(ModelMember).filter(ModelMember.id_user == id_user, ModelMember.id_ == id_).first()

# функция добавления участника по схеме с сохранением в бд
def crud_member_create(db: Session, Member: SchemMemberCreate):
    db_Member = ModelMember(Member.user_id,Member._id)
    db.add(db_Member)
    db.commit()
    db.refresh(db_Member)
    return db_Member
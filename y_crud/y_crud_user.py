# импорты библиотек
from sqlalchemy.orm import Session
# импорт модели
from y_model.y_model_user import ModelUser
# импорт схемы
from y_schem.y_schem_user import SchemUserCreate

# функция получения пользователя по id
def crud_user_get_by_id(db: Session, id: int):
    return db.query(ModelUser).filter(ModelUser.id == id).first()

# функция получения пользователя по логину
def crud_user_get_by_login(db: Session, login: str):
    return db.query(ModelUser).filter(ModelUser.login == login).first()

# функция получения пользователей по никнейму
def crud_user_get_by_nickname(db: Session, nickname: str):
    return db.query(ModelUser).filter(ModelUser.nickname == nickname).all()

# функция добавления пользователя по схеме с сохранением в бд
def crud_user_create(db: Session, user: SchemUserCreate):
    db_user = ModelUser(login = user.login, password = user.password, nickname = user.nickname)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
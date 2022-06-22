# импорт библиотек
from sqlalchemy import *
from sqlalchemy.orm import *
# создание файла бд sqlite
db_engine = create_engine('sqlite:///messenger.sqlite',connect_args={'check_same_thread': False})
# созадние сессии с бд
db_session = sessionmaker()()
# декларирование бд
db = declarative_base(bind=db_engine)
# создание моделей
import y_model.y_model_user
import y_model.y_model_chat
import y_model.y_model_message
import y_model.y_model_chat_member
# создание таблиц
db.metadata.create_all(db_engine)


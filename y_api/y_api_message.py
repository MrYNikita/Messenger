# импорт библиотек
from fastapi import *
from fastapi.requests import *
from fastapi.responses import *
# импорт
from y_db import *
from y_manager import api
import y_api.y_api
# импорт схем
from y_schem.y_schem_message import *
# импорт CRUD
from y_crud.y_crud_message import *
# создание роутера
api_router_message = APIRouter(prefix='/message',tags=['message'])

@api.post('/message/', response_model=SchemMessage)
def api_message_create(message: SchemMessageCreate):
    return crud_message_create(db_session,message)
# импорт библиотек
from fastapi import *
from fastapi.requests import *
from fastapi.responses import *
# импорт
from y_db import *
from y_manager import api
import y_api.y_api
# импорт схем
from y_schem.y_schem_member import *
# импорт CRUD
from y_crud.y_crud_member import *
# создание роутера
api_router_member = APIRouter(prefix='/member',tags=['member'])

@api.get('/chat/id_user_one/{id_user_one}/id_user_two/{id_user_two}')
async def api_get_chat_by_users(id_user_one: int, id_user_two: int):
    return null
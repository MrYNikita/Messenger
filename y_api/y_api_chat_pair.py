# импорт библиотек
from fastapi import *
from fastapi.requests import *
from fastapi.responses import *
# импорт
from y_db import *
from y_manager import api
import y_api.y_api
# импорт схем
from y_schem.y_schem_chat import *
# импорт CRUD
from y_crud.y_crud_chat import *
from y_crud.y_crud_member import *
from y_crud.y_crud_chat_pair import *
# создание роутера
api_router_chat_pair = APIRouter(prefix='/chat_pair',tags=['chat_pair'])

@api.post("/chat_pair/", response_model=SchemChatPair)
def api_user_create(chat: SchemChatPairCreate):
    print(chat)
    return crud_chat_pair_create(db_session,chat)

@api.get('/chat_pair/user/id_user_one/{id_user_one}/id_user_two/{id_user_two}')
async def api_get_chat_by_users(id_user_one: int, id_user_two: int):
    chat = crud_chat_pair_get_by_users(db_session,id_user_one,id_user_two)
    if (type(chat) == ModelChatPair):
        return chat
    else:
        return HTMLResponse(status_code=404)
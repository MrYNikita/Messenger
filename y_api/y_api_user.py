# импорт библиотек
from fastapi import *
from fastapi.requests import *
from fastapi.responses import *
# импорт
from y_db import *
from y_manager import api
import y_api.y_api
# импорт схем
from y_schem.y_schem_user import *
# импорт CRUD
from y_crud.y_crud_user import *
# создание роутера
api_router_user = APIRouter(prefix='/user',tags=['user'])

@api.post("/user/", response_model=SchemUser)
def api_user_create(user: SchemUserCreate):
    return crud_user_create(db_session,user)

@api.get('/user/id/{id}', response_model=SchemUser)
async def api_user_get_by_id(id: int):
    return crud_user_get_by_id(db_session,id)

@api.get('/user/nickname/{nickname}', response_model=list[SchemUser])
def api_user_get_by_nickname(nickname: str):
    return crud_user_get_by_nickname(db_session,nickname)

@api.get('/user/login/{login}/password/{password}', response_model=SchemUser)
async def api_user_authorizate(login: str, password: str):
    user = crud_user_get_by_login(db_session,login)
    if user.password == password:
        return user
    else:
        return HTMLResponse(status_code=401)

@api.get('/user/authorizate/login/{login}/password/{password}', response_class=HTMLResponse)
async def api_user_redirect(request: Request, login: str, password: str):
    user = await api_user_authorizate(login,password)
    if type(user) == ModelUser:
        return y_api.y_api.api_templates.TemplateResponse('y_user.html', { 'request': request, 'data': user })
    else:
        return HTMLResponse(status_code=401)
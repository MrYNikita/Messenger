# импорты
from y_manager import api
# импорты библиотек
from fastapi import *
from fastapi.requests import *
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import *
# добавление статических файлов
api.mount('/y_source', StaticFiles(directory='y_source'), name='y_source')
# добавление шаблонов
api_templates = Jinja2Templates(directory='y_source/y_html')

@api.get('/')
async def redirect_home():
    return RedirectResponse('http://localhost:8000/sigin')

@api.get('/login')
async def redirect_login():
    return HTMLResponse(open('./y_source/y_html/y_login.html','r',encoding='utf8').read())
    
@api.get('/sigin')
async def redirect_sigin():
    return HTMLResponse(open('./y_source/y_html/y_sigin.html','r',encoding='utf8').read())

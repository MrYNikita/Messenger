# импорты библиотек
import os
import fastapi
import uvicorn
# импорты файлов
import y_db
import y_api.y_api
# очистка консоли
os.system('cls')
# создание api
api = fastapi.FastAPI()
# запуск сервера uvicorn
if __name__ == '__main__': uvicorn.run(app='y_manager:api', host='127.0.0.1', port=8000, reload=True, debug=True)
# импорты роутеров
from y_api.y_api_user import api_router_user
from y_api.y_api_chat import api_router_chat
from y_api.y_api_member import api_router_member
# подключение роутеров
api.include_router(api_router_user)
api.include_router(api_router_chat)
api.include_router(api_router_member)
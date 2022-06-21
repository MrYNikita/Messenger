# импорты библиотек
import os
import fastapi
import uvicorn
# импорты файлов
import y_db
import y_api.y_api
# импорты роутеров
from y_api.y_api_user import api_router_user
# очистка консоли
os.system('cls')
# создание api
api = fastapi.FastAPI()
# подключение роутеров
api.include_router(api_router_user)
# запуск сервера uvicorn
if __name__ == '__main__': uvicorn.run(app='y_manager:api', host='127.0.0.1', port=8000, reload=True, debug=True)
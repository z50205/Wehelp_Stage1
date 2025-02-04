from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from routers import router
from starlette.middleware.sessions import SessionMiddleware
import os

load_dotenv()
SECRETKEY = os.environ.get("SECRETKEY","1234")
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(router)
app.add_middleware(SessionMiddleware, secret_key=SECRETKEY)




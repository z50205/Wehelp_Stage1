from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,RedirectResponse
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


@app.exception_handler(404)
async def notfound(request:Request, exc: Exception):
    redirect_url=request.url_for('signin_error').include_query_params(message="404") 
    return RedirectResponse(redirect_url,status_code=303)

@app.exception_handler(405)
async def notfound(request:Request, exc: Exception):
    redirect_url=request.url_for('signin_error').include_query_params(message="405") 
    return RedirectResponse(redirect_url,status_code=303)



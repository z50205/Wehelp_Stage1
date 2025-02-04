from fastapi import APIRouter, Request,Form
from typing import Annotated
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.requests import HTTPConnection
from starlette.templating import Jinja2Templates
import os
from models import UserData

templates_path=os.path.join("..",os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],"templates")
router = APIRouter()
templates = Jinja2Templates(directory=templates_path)

@router.get("/", response_class=HTMLResponse, tags=["index"])
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@router.post("/signin", response_class=HTMLResponse, tags=["signin"])
async def signin_user(request: Request,userdata:UserData=Form()):
    if userdata.username=="test" and userdata.password=="test" :
        request.session["SIGNED-IN"]=True
        redirect_url=request.url_for('signin_success') 
        return RedirectResponse(redirect_url,status_code=303)
    elif not (userdata.username and userdata.password):
        redirect_url=request.url_for('signin_error').include_query_params(message="missing") 
        return RedirectResponse(redirect_url,status_code=303)
    else:
        redirect_url=request.url_for('signin_error').include_query_params(message="loginfail")
        return RedirectResponse(redirect_url,status_code=303)

@router.get("/member", response_class=HTMLResponse, tags=["loginsuccess"])
async def signin_success(request: Request):
    if "SIGNED-IN" not in request.session:
        request.session["SIGNED-IN"]=False
    if request.session["SIGNED-IN"]==True:
        return templates.TemplateResponse(
            request=request, name="success.html"
        )
    else:
        redirect_url=request.url_for('index')
        return RedirectResponse(redirect_url,status_code=303)

@router.get("/error", response_class=HTMLResponse, tags=["loginerror"])
async def signin_error(request: Request,message:str):
    if message=="missing":
        showMessage="帳號或密碼未輸入，請重新輸入"
    elif message=="loginfail":
        showMessage="帳號或密碼錯誤"
    return templates.TemplateResponse(
        request=request, name="error.html",context={"message": showMessage}
    )
@router.get("/signout", response_class=HTMLResponse, tags=["signout"])
async def signout(request: Request):
    request.session["SIGNED-IN"]=False
    redirect_url=request.url_for('index')
    return RedirectResponse(redirect_url,status_code=303)

@router.get("/square/{posStr}", response_class=HTMLResponse, tags=["calculate"])
async def calculate(request: Request,posStr:str):
    try:
        posInt=int(posStr)
        if posInt>0:
            result=posInt*posInt
            return templates.TemplateResponse(
                request=request, name="calculate.html",context={"result": result})
    except:
        pass
    redirect_url=request.url_for('index')
    return RedirectResponse(redirect_url,status_code=303)


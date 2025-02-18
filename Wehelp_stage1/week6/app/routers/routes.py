from fastapi import APIRouter, Request,Form,Depends,HTTPException
from typing import Annotated
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.requests import HTTPConnection
from starlette.templating import Jinja2Templates
import os
from models import UserData,MessageData

templates_path=os.path.join("..",os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],"templates")
router = APIRouter()
templates = Jinja2Templates(directory=templates_path)

def login_required(request:Request):
    if "User" not in request.session:
        redirect_loc='/'
        raise HTTPException(status_code=303, detail="Authorization Failed.", headers={"Location": redirect_loc})

@router.get("/", response_class=HTMLResponse, tags=["index"])
async def index(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html"
    )

@router.post("/signup", response_class=HTMLResponse, tags=["signup"])
async def signin_user(request: Request,userdata: Annotated[UserData, Form()]):
    u=UserData.query_username(userdata.username)
    if u == None:
        UserData.create_user(userdata)
        redirect_url=request.url_for('index')
        return RedirectResponse(redirect_url,status_code=303)
    else:
        redirect_url=request.url_for('signin_error').include_query_params(message="repeated") 
        return RedirectResponse(redirect_url,status_code=303)

@router.post("/signin", response_class=HTMLResponse, tags=["signin"])
async def signin_user(request: Request,userdata: Annotated[UserData, Form()]):
    u=UserData.query_username(userdata.username)
    if not (userdata.username and userdata.password):
        redirect_url=request.url_for('signin_error').include_query_params(message="missing") 
        return RedirectResponse(redirect_url,status_code=303)
    elif u == None:
        redirect_url=request.url_for('signin_error').include_query_params(message="loginfail")
        return RedirectResponse(redirect_url,status_code=303)
    elif u.check_pw(userdata.password):
        request.session["User"]=[u.id,u.name,u.username]
        redirect_url=request.url_for('signin_success') 
        return RedirectResponse(redirect_url,status_code=303)
    else:
        redirect_url=request.url_for('signin_error').include_query_params(message="loginfail")
        return RedirectResponse(redirect_url,status_code=303)

@router.get("/member", response_class=HTMLResponse,dependencies=[Depends(login_required)], tags=["loginsuccess"])
async def signin_success(request: Request):
        messages=MessageData.query_messages()
        print(request.session["User"])
        return templates.TemplateResponse(request=request, name="success.html",context={"name": request.session["User"][1],"messages":messages})

@router.get("/error", response_class=HTMLResponse, tags=["loginerror"])
async def signin_error(request: Request,message:str):
    if message=="missing":
        showMessage="帳號或密碼未輸入，請重新輸入"
    elif message=="loginfail":
        showMessage="帳號或密碼錯誤"
    elif message=="repeated":
        showMessage="帳號已使用過"
    elif message=="404":
        showMessage="頁面未找到"
    elif message=="405":
        showMessage="未開放此功能"
    return templates.TemplateResponse(
        request=request, name="error.html",context={"message": showMessage}
    )
@router.get("/signout", response_class=HTMLResponse,dependencies=[Depends(login_required)], tags=["signout"])
async def signout(request: Request):
    del request.session["User"]
    redirect_url=request.url_for('index')
    return RedirectResponse(redirect_url,status_code=303)

@router.post("/createMessage", response_class=HTMLResponse,dependencies=[Depends(login_required)], tags=["createmessage"])
async def create_message(request: Request,message: str=Form(...)):
    MessageData.create_message(member_id=request.session["User"][0],message=message)
    redirect_url=request.url_for('signin_success')
    return RedirectResponse(redirect_url,status_code=303)

@router.post("/deleteMessage", response_class=HTMLResponse,dependencies=[Depends(login_required)], tags=["deletemessage"])
async def delete_message(request: Request,id:int=Form(...)):
    mes=MessageData.query_message(id)
    if request.session["User"][0]==mes.member_id:
        MessageData.delete_message(id)
    redirect_url=request.url_for('signin_success')
    return RedirectResponse(redirect_url,status_code=303)


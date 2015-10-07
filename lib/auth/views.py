# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods
from lib.core.views import JSONResponse
from django.contrib.auth.models import User as DUser
from lib.auth.models import CustomUser
from lib.auth.forms import *
from django.http import HttpResponse, HttpResponseRedirect
# from django.http import Http404


@require_http_methods(["POST"])
def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JSONResponse({"status" : "200", "message": "ok", "user": {"username": user.username, "cash": CustomUser.objects.get(userid=user).cash }})
        else:
            return JSONResponse({"status" : "201", "message" : u"Ваш аккаунт не активирован. Чтобы активировать ваш аккаунт перейдите по ссылке, указанной в письме.", "user": {"username": user.username, "cash": CustomUser.objects.get(userid=user).cash }})
    else:
        return JSONResponse({"status" : "403", "messga" : u"Неправильный логин/пароль."})

@require_http_methods(["POST"])
def auth_registration(request):
    if request.user.is_authenticated():
        return JSONResponse({"status" : "200", "user": {"username": user.username, "cash": CustomUser.objects.get(userid=user).cash }})
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    if DUser.objects.filter(username=username) or DUser.objects.filter(email=email): 
        return JSONResponse({"status": "201", "message": u"Имя уже существует"})

    if not username:
        return JSONResponse({"status": "400", "message": u"Введите имя пользователя."})
    if not password:
        return JSONResponse({"status": "400", "message": u"Введите пароль."})
    if not email:
        return JSONResponse({"status": "400", "message": u"Введите адрес вашей электронной почты."})

    user = DUser.objects.create_user(username, email, password)
    CustomUser.objects.create(userid=user, cache=0,rating=0)
    return JSONResponse({"status" : "200", "user": {"username": user.username, "cash": CustomUser.objects.get(userid=user).cash }})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def auth_set_avatar(request):
    avatar=ImageUploadForm(request.POST, request.FILES)
    curuser=CustomUser.objects.get(userid=request.user)
    curuser.avatar = request.FILES['avatar']
    curuser.save()
    return HttpResponseRedirect('/') 

# coding=utf-8
import datetime
import uuid

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import User as DUser
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from lib.auth.forms import *
from lib.auth.models import CustomUser, EmailApprove
from lib.core.views import JSONResponse

# from django.http import Http404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate 


@require_http_methods(["POST"])
def auth_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JSONResponse({'status': "200", "redirect": reverse("map")})  # JSONResponse({"status" : "200", "message": "ok", "user": {"username": user.username, "cash": CustomUser.objects.get(user=user).cash }})
        else:
            return JSONResponse({"status" : "201", "message" : u"Ваш аккаунт не активирован. Чтобы активировать ваш аккаунт перейдите по ссылке, указанной в письме.", "user": {"username": user.username, "cash": CustomUser.objects.get(user=user).cash }})
    else:
        return JSONResponse({"status" : "403", "message" : u"Неправильный логин/пароль."})


@require_http_methods(["POST"])
def auth_registration(request):
    if request.user.is_authenticated():
        return JSONResponse({"status" : "200", "user": {"username": request.user.username, "cash": request.usr.cash}, "redirect": "/map/"})
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    if DUser.objects.filter(username=username): 
        return JSONResponse({"status": "400", "message": u"Имя уже существует"})

    if DUser.objects.filter(email=email): 
        return JSONResponse({"status": "400", "message": u"Email уже занят"})

    if not username:
        return JSONResponse({"status": "400", "message": u"Введите имя пользователя."})
    if not password:
        return JSONResponse({"status": "400", "message": u"Введите пароль."})
    if not email:
        return JSONResponse({"status": "400", "message": u"Введите адрес вашей электронной почты."})

    user = DUser.objects.create_user(username, email, password)
    cuser = CustomUser.objects.create(user=user, cash=0, rating=0)

    approve_value = uuid.uuid4().hex[:255]
    EmailApprove.objects.create(user=cuser, value=approve_value)
    send_mail('test email', "%s%s?hash=%s" % (settings.HOST, reverse('auth-approve-email'), approve_value), 'admin@enggeo.ru', [email]) 
    
    ruser = authenticate(username=username, password=password)
    login(request, ruser)
    return JSONResponse({'status': "200", "redirect": reverse("map")})


def approve_email(request):
    approve = EmailApprove.objects.filter(value=request.GET.get('hash', '')).first()
    if approve and (approve.date.replace(tzinfo=None) - datetime.datetime.now()).days < 1:
        approve.user.is_registered = True
        approve.user.save()
        approve.delete()
        return render(request, 'auth/approve.html', {'status': True, 'message': u'Успешно!'})
    return render(request, 'auth//approve.html', {'status': False, 'message': u'К сожалению такого кода нет'})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def auth_set_avatar(request):
    form = ImageUploadForm(request.POST, request.FILES)
    if form.is_valid():
        request.usr.avatar = request.FILES['avatar']
    return HttpResponseRedirect('/') 

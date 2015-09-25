# coding=utf-8
from django.contrib.auth import authenticate, login
from django.views.decorators.http import require_http_methods
from lib.core.views import JSONResponse
from django.contrib.auth.models import User as DUser
from lib.auth.models import User
# from django.http import Http404


@require_http_methods(["POST"])
def ajax_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JSONResponse({"status" : "200", "message": "ok", "user": {"username": user.username, "cache": User.objects.get(django_user=user).cache }})
        else:
            return JSONResponse({"status" : "201", "message" : "You need to activate your account. Please check your email", "user": {"username": user.username, "cache": User.objects.get(django_user=user).cache }})
    else:
        return JSONResponse({"status" : "403", "messga" : "Invalid username/password"})

@require_http_methods(["POST"])
def ajax_registration(request):
    if request.user.is_authenticated():
        return JSONResponse({"status" : "200", "user": {"username": user.username, "cache": User.objects.get(django_user=user).cache }})
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    if DUser.objects.filter(username=username) or DUser.objects.filter(email=email): 
        return JSONResponse({"status": "201", "message": u"Имя уже существует"})

    if not username:
        return JSONResponse({"status": "400", "message": "No username"})
    if not password:
        return JSONResponse({"status": "400", "message": "No password"})
    if not email:
        return JSONResponse({"status": "400", "message": "No email"})

    user = DUser.objects.create_user(username, email, password)
    User.objects.create(email=email, django_user=user, cache=0)
    return JSONResponse({"status" : "200", "user": {"username": user.username, "cache": User.objects.get(django_user=user).cache }})


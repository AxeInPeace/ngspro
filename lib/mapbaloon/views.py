from django.contrib.auth import *
from django.shortcuts import render
from models import *
from forms import *
from lib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect


def map(request):
    baloons = baloon.objects.all()
    if request.method == "GET":
        if request.user.is_authenticated():
            frmat = formats.objects.all()
            tools = instruments.objects.all()
            my_rating = User.objects.get(django_user=request.user).getRating()
            
            context = {		
                "formats": frmat,
                "tools": tools,
                "baloons": baloons,
                "signin_error": None,
                "my_rating": my_rating,				
                "user": request.user,			
            }
            return render(request, 'index.html', context)		
        context = {		
            "baloons": baloons,
            "signin_error": None,
            "signin_form": SigninForm(),
        }
        return render(request, 'index.html', context)


def fun_logout(request):
	logout(request)	
	return HttpResponseRedirect("/")



from django.contrib.auth import *
from django.shortcuts import render
from .models import *
from .forms import *
from lib.auth.models import User

from lib.auth.models import CustomUser
import datetime
from django.http import HttpResponse, HttpResponseRedirect


def map(request):
    balloons = Balloon.objects.all()
    if request.method == "GET":
        if request.user.is_authenticated():
            frmat = Format.objects.all()
            tools = Instrument.objects.all()
	    custuser = CustomUser.objects.get(userid=request.user) 
            my_cash = custuser.cash
	    my_rating = custuser.rating            
	    avatar = custuser.avatar
            context = {		
                "formats": frmat,
                "tools": tools,
                "balloons": balloons,
                "signin_error": None,
                "my_cash": my_cash,				
		"my_rating": my_rating,
                "user": request.user,			
		"avatar": avatar,
            }
            return render(request, 'index.html', context)		
        context = {		
            "balloons": balloons,
            "signin_error": None,
            "signin_form": SigninForm(),
        }
        return render(request, 'index.html', context)


def fun_logout(request):
	logout(request)	
	return HttpResponseRedirect("/")

def addBalloon(request):
    if request.method == "POST":
        fr = Format.objects.get(id=request.POST['frm'])
	tl = Instrument.objects.get(id=request.POST['tool'])
	pub = CustomUser.objects.get(userid=request.user)
	Balloon.objects.create(
	    coord1=request.POST['coord1'],
	    coord2=request.POST['coord2'],
	    isugrshoot=request.POST['ugbool'],
	    isaltmark=request.POST['altbool'],
	    isrelelems=request.POST['relbool'],
	    syscoord=request.POST['altsys'],
	    sysaltit=request.POST['coordsys'],
	    myFormat=fr,
	    instrument=tl,
	    publisher=pub,
	    date=datetime.datetime.now().date(),
	)    
    return HttpResponseRedirect("/")

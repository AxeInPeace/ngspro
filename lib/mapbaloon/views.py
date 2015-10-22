# encoding=utf-8
from django.contrib.auth import *
from django.shortcuts import render
from .models import *
from .forms import *
from lib.auth.models import User

from lib.auth.models import CustomUser
import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def mapballoon_map(request):
    balloons = Balloon.objects.all()
    trgstations = TriangulationStation.objects.all()
    
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
            "trgstations": trgstations,
        }
        return render(request, 'mapbaloon/index.html', context)		
    context = {		
        "balloons": balloons,
        "signin_error": None,
        "signin_form": SigninForm(),
    }
    return render(request, 'mapbaloon/index.html', context)



#TODO: превратить в ajax
@require_http_methods(["POST"])
def mapballoon_add_balloon(request):
    if not request.user.is_authenticated():
        raise Http404
    fr = Format.objects.get(id=request.POST['frm'])
    tl = Instrument.objects.get(id=request.POST['tool'])
    pub = CustomUser.objects.get(userid=request.user)
    Balloon.objects.create(
        lat=request.POST['coord1'],
        lng=request.POST['coord2'],
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

@require_http_methods(["POST"])
def mapballoon_add_trgpoint(request):
    if not request.user.is_authenticated():
        raise Http404
    pub = CustomUser.objects.get(userid=request.user)
    if(request.POST['trggov'] == "gover"):
        govtype = True
    else:
        govtype = False

    TriangulationStation.objects.create(
        lat=request.POST['trgcoord1'],
        lng=request.POST['trgcoord2'],
        title=request.POST['trgname'],
        type=request.POST['trgtype'],
        precision=request.POST['trgaccuracy'],
        height=request.POST['trgheight'],
        national=govtype,
        backsight=(request.POST['trgorientstate']=="save"),
        outer=(request.POST['trgoutstate']=="save"),
        center=(request.POST['trgcenterstate']=="save"),
        center_height=request.POST['trgcenterplace'],
        center_photo=Photo.objects.get(id=1),
        publisher=pub,
        date=datetime.datetime.now().date(),
    )    
    return HttpResponseRedirect("/")


@require_http_methods(["POST"])
def mapballoon_filter_for_years(request):
    if request.POST['year']:
        trgstations = TriangulationStation.objects.all()
        balloons = Balloon.objects.filter(date__year=request.POST['year'])
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
                "trgstations": trgstations,
            }
            return render(request, 'mapbaloon/index.html', context)		
        context = {		
            "balloons": balloons,
            "signin_error": None,
            "signin_form": SigninForm(),
        }
        return render(request, 'mapbaloon/index.html', context)
    else:
        return HttpResponseRedirect("/")


@require_http_methods(["POST"])
def mapballoon_filter_for_formats(request):
    if request.POST['format']:
        trgstations = TriangulationStation.objects.all()
        balloons = Balloon.objects.filter(myFormat=int(request.POST['format']))
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
                "trgstations": trgstations,
            }
            return render(request, 'mapbaloon/index.html', context)		

# encoding=utf-8
from django.contrib.auth import *
from django.shortcuts import render
from .models import *
from .forms import *
from lib.auth.models import User
from json import loads
from lib.core.views import JSONResponse

from lib.auth.models import CustomUser
import datetime
from django.http import HttpResponse, Http404
from django.views.decorators.http import require_http_methods
from lib.core.utils import  upload_file
from lib.photo.models import Photo
from django.shortcuts import redirect


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
    else:
        return redirect('main')

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
    fr = Format.objects.get(id=request.POST.get('frm'))
    tl = Instrument.objects.get(id=request.POST.get('tool'))
    pub = CustomUser.objects.get(userid=request.user)
    
    material_photo = request.POST.get("photo")
    if material_photo is not None:
        photo_url = upload_file(material_photo, material_photo.name, ["jpg", "jpeg", "png"])
    else:
        photo_url = None

    material_photo_url = Photo.objects.create(url=photo_url, alt=u"Фото центра")

    material = request.POST.get("material")
    if material is not None:
        material_url = upload_file(material, material.name, ["rar", "zip"])
    else:
        material_url = None

    material_url = Photo.objects.create(url=material_url, alt=u"Фото центра")

    Balloon.objects.create(
        lat=request.POST.get('coord1'),
        lng=request.POST.get('coord2'),
        isugrshoot=request.POST.get('ugbool'),
        isaltmark=request.POST.get('altbool'),
        isrelelems=request.POST.get('relbool'),
        syscoord=request.POST.get('altsys'),
        sysaltit=request.POST.get('coordsys'),
        title=request.POST.get('title'), 
        myFormat=fr,
        instrument=tl,
        publisher=pub,
        date=datetime.datetime.now().date(),
        material_photo=material_photo_url,
        material=material_url,
    )    
    return JSONResponse({'status': 200, 'message': 'ok'})


@require_http_methods(["POST"])
def mapballoon_add_trgpoint(request):
    if not request.user.is_authenticated():
        raise Http404
    print request.POST.items()
    pub = CustomUser.objects.get(userid=request.user)

    lat=request.POST.get('trgcoord1')
    lng=request.POST.get('trgcoord2')

    material_photo = request.POST.get("photo")
    if material_photo is not None:
        photo_url = upload_file(material_photo, material_photo.name, ["jpg", "jpeg", "png"])
    else:
        photo_url = None

    material_photo_id = Photo.objects.create(url=photo_url, alt=u"Фото центра")
    material_photo = Photo.objects.create(url=url_photo, alt="")

    same_station = TriangulationStation.objects.filter(lat=lat, lng=lng)
    if same_station:
        return JSONResponse({'status': 300, 'message': 'В этом месте уже есть тригопункт', '': same_station})
    

    TriangulationStation.objects.create(
        lat=lat,
        lng=lng,
        title=request.POST.get('trgname'),
        type=request.POST.get('trgtype'),
        precision=request.POST.get('trgaccuracy'),
        height=request.POST.get('trgheight'),
        national=(request.POST.get('trggov') == "gover"),
        backsight=(request.POST.get('trgorientstate') == "save"),
        outer=(request.POST.get('trgoutstate') == "save"),
        center=(request.POST.get('trgcenterstate') == "save"),
        center_height=request.POST.get('trgcenterplace'),
        center_photo=material_photo_id,
        publisher=pub,
        date=datetime.datetime.now().date(),
    )    
    return redirect('map')


@require_http_methods(["POST"])
def mapballoon_filter_for_years(request):
    if request.POST.get('year'):
        trgstations = TriangulationStation.objects.all()
        balloons = Balloon.objects.filter(date__year=request.POST.get('year'))
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
        return redirect('map')


@require_http_methods(["POST"])
def mapballoon_filter_for_formats(request):
    if request.POST.get('format'):
        trgstations = TriangulationStation.objects.all()
        balloons = Balloon.objects.filter(myFormat=int(request.POST.get('format')))
        if not request.user.is_authenticated():
            raise Http404
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

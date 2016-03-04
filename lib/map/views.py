# encoding=utf-8

import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView

from lib.core.utils import upload_file
from lib.core.views import JSONResponse
from lib.map.serializers import serialize_trg
from .models import *


@require_http_methods(["GET"])
def mapballoon_map(request):
    balloons = Balloon.objects.all()
    trgstations = TriangulationStation.objects.all()

    if request.user.is_authenticated():
        frmat = Format.objects.all()
        tools = Instrument.objects.all()
        custuser = CustomUser.objects.get(user=request.user)
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
        return render(request, 'map/index.html', context)
    else:
        return redirect('main')


@require_http_methods(["POST"])
def mapballoon_add_balloon(request):
    if not request.user.is_authenticated():
        raise Http404
    fr = Format.objects.filter(id=request.POST.get('frm')).first()
    tl = Instrument.objects.filter(id=request.POST.get('tool')).first()
    pub = CustomUser.objects.filter(user=request.user).first()

    if not fr:
        return JSONResponse({'status': 301, 'message': u'Такого формата не существует'})

    if not tl:
        return JSONResponse({'status': 301, 'message': u'Такого иструмента не существует'})

    if not pub:
        return JSONResponse({'status': 301, 'message': u'Вы не авторизованы?'})

    material_photo = request.FILES.get("photo")
    if material_photo is not None:
        photo_url = upload_file(material_photo, material_photo.name, ["jpg", "jpeg", "png"])
    else:
        photo_url = None

    material_photo_url = Photo.objects.create(url=photo_url, alt=u"Фото центра")

    material = request.FILES.get("material")
    if material is not None:
        material_url = upload_file(material, material.name, ["pdf"])
    else:
        material_url = None
    if not material_url:
        return JSONResponse({'status': 401, 'message': u'Не загружен материал и/или не совпадает формат'})
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
    return JSONResponse({'status': "200", "redirect": reverse("map")});


@require_http_methods(["POST"])
def mapballoon_add_trgpoint(request):
    # Переехать на форму
    if not request.user.is_authenticated():
        raise Http404
    pub = CustomUser.objects.get(user=request.user)

    lat = request.POST.get('trgcoord1')
    lng = request.POST.get('trgcoord2')
    if not lng or not lat:
        return JSONResponse({'status': 401, 'message': u'Не введены координаты'})

    title = request.POST.get('trgname', '%s, %s' % (lat, lng))
    if not title:
        return JSONResponse({'status': 401, 'message': u'Не указано название'})

    material_photo = request.FILES.get("photo")
    if material_photo is not None:
        photo_url = upload_file(material_photo, material_photo.name, ["jpg", "jpeg", "png"])
        material_photo_id = Photo.objects.create(url=photo_url, alt=u"Фото центра")
    else:
        material_photo_id = None

    same_station = TriangulationStation.objects.filter(lat=lat, lng=lng)
    if same_station:
        return JSONResponse({'status': 300, 'message': 'В этом месте уже есть тригопункт', '': same_station.title})

    precision = request.POST.get('trgaccuracy') if request.POST.get('trgaccuracy') and request.POST.get('trgaccuracy') != 'u' else None
    height = request.POST.get('trgheight') if request.POST.get('trgheight') and request.POST.get('trgheight') != 'u' else None
    national = (request.POST.get('trggov') == "gover") if request.POST.get('trggov') and request.POST.get('trggov') != 'u' else None
    backsight = (request.POST.get('trgorientstate') == "save") if request.POST.get('trgorientstate') and request.POST.get('trgorientstate') != 'u' else None
    outer = (request.POST.get('trgoutstate') == "save") if request.POST.get('trgoutstate') and request.POST.get('trgoutstate') != 'u' else None
    center = (request.POST.get('trgcenterstate') == "save") if request.POST.get('trgcenterstate') and request.POST.get('trgcenterstate') != 'u' else None
    center_height = request.POST.get('trgcenterplace') if request.POST.get('trgcenterplace') and request.POST.get('trgcenterplace') != 'u' else None
    TriangulationStation.objects.create(
        lat=lat,
        lng=lng,
        title=title,
        type=request.POST.get('trgtype'),
        precision=precision,
        height=height,
        national=national,
        backsight=backsight,
        outer=outer,
        center=center,
        center_height=center_height,
        center_photo=material_photo_id,
        publisher=pub,
        date=datetime.datetime.now().date(),
    )

    return JSONResponse({'status': "200", "redirect": reverse("map")});


class MaterialJsonList(TemplateView):
    template_name = 'map/map_tile_response.html'
    model = TriangulationStation
    content_type = 'application/json'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.years = request.GET.getlist('year')
        self.bbox = request.GET.get('bbox')
        return super(MaterialJsonList, self).dispatch(request, *args, **kwargs)

    def _get_years_filter(self):
        q_filter = Q()
        if self.years:
            for year in self.years:
                q_filter = q_filter | (
                Q(date__gte=datetime.date(int(year), 1, 1)) & Q(date__lt=datetime.date(int(year) + 1, 1, 1)))
        return q_filter

    def get_topo(self):
        """
        Список наших объектов будет состоять лишь из приватных и не удаленных статей
        """
        q_filter = self._get_years_filter()

        return Balloon.objects.filter(is_published=True).filter(q_filter)

    def get_trg(self):
        """
        Список наших объектов будет состоять лишь из приватных и не удаленных статей
        """
        q_filter = Q()
        filters = {}
        if self.years:
            for year in self.years:
                q_filter = q_filter | (
                Q(date__gte=datetime.date(int(year), 1, 1)) & Q(date__lt=datetime.date(int(year) + 1, 1, 1)))
        if self.bbox:
            pass
        return [serialize_trg(trg) for trg in TriangulationStation.objects.filter(is_published=True).filter(q_filter, **filters)]

    def get_context_data(self, **kwargs):
        data = super(MaterialJsonList, self).get_context_data()
        data['trg_list'] = self.get_trg()
        data['topo_list'] = self.get_topo()
        data['show_download'] = self.request.usr.is_registered
        data['callback'] = self.request.GET['callback']
        return data

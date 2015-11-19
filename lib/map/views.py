# encoding=utf-8
import json

from django.shortcuts import render
from django.template.loader import render_to_string

from lib.mapbaloon.models import TriangulationStation
from .utils import serialize_trg


def get_trg(request):
    bbox = request.GET['bbox']
    response = {
        'callback': request.GET['callback'],
        'data': TriangulationStation.objects.all()
    }
    return render(request, 'inc/map_tile_response.json', response, content_type='application/json')


def get_materials(request):
    bbox = request.GET['bbox']
    response = {
        'callback': request.GET['callback'],
        'data': TriangulationStation.objects.all()
    }
    return render(request, 'inc/map_tile_response.json', response, content_type='application/json')

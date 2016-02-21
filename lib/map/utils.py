# encoding=utf-8
from django.utils.formats import date_format


def serialize_trg(trg):
    trgp = {
        "type": "Feature",  # !?
        "id": trg.id,
        "geometry": {
            "coordinates": [trg.lat, trg.lng],
            "type": "Point"
        },
        "properties": {
            "balloonContentHeader": trg.title,
            "balloonContentBody": u''.join((u"Ширина: ", unicode(trg.lat), u"<br>Долгота: ", unicode(trg.lng), u"<br>Тип: ", trg.get_type_display(), u"<br>Класс точности:", unicode(trg.precision), u"<br>Высота над уровнем моря: " , unicode(trg.height), u", м<br>date = ", trg.date.strftime("%d.%m.%Y"))), 
            "clusterCaption": u"Метка 2"
        }, 
        "options": {
            "iconLayout": 'default#image',
            "iconImageHref": 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Japanese_Map_symbol_(Triangulation_point).svg/2000px-Japanese_Map_symbol_(Triangulation_point).svg.png',
            "iconImageSize": [32, 32],
            "iconImageOffset": [-16, -16]
        }
    }
    if trg.center_photo:
        trgp['properties']["balloonContentFooter"] = u"<a href='" + unicode(trg.center_photo.url) + u"' class='fancybox' title='Фото центра'><img src='" + unicode(trg.center_photo.url) + u"' width='128' height='128'/></a>"
    return trgp

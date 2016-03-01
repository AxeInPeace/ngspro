# coding=utf-8
def serialize_trg(trg):
    return {
        'id': trg.pk,
        'lat': trg.lat,
        'lng': trg.lng,
        'title': trg.title,
        'type': trg.get_type_display(),
        'precision': trg.precision if trg.precision else 'неизвестно',
        'backsight': "сохранился" if trg.backsight else "нет данных" if trg.backsight is None else "не сохранился",
        'outer': "сохранился" if trg.outer else "нет данных" if trg.outer is None else "не сохранился",
        'center': "сохранился" if trg.center else "нет данных" if trg.center is None else "не сохранился",
        'center_height': trg.center_height if trg.center_height is not None else "нет данных",
        'images': [{'url': img.url} for img in trg.images],
    }

import json

from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data):
        content = json.dumps(data, ensure_ascii=False)
        super(JSONResponse, self).__init__(content=content, content_type='application/json; charset=utf-8')


class Enggeo(object):
    def get_context_data(self, **kwargs):
        data = super(Enggeo, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            data.update({
                'avatar': self.request.usr.avatar
            })
        return data
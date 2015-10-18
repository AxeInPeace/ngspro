import json

from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data):
        content = json.dumps(data, ensure_ascii=False)
        super(JSONResponse, self).__init__(content=content, content_type='application/json; charset=utf-8')


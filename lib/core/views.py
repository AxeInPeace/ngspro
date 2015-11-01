import json
import uuid


from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lib.photo.models import Photo
from lib.core.utils import upload_file


class JSONResponse(HttpResponse):
    def __init__(self, data):
        content = json.dumps(data, ensure_ascii=False)
        print data
        super(JSONResponse, self).__init__(content=content, content_type='application/json; charset=utf-8')

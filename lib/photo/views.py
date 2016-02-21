import uuid

from gcloud import storage
from PIL import Image
import StringIO

from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from json import loads

from lib.core.views import JSONResponse
from lib.core.utils import upload_file
from lib.photo.models import Photo
from lib.auth.models import CustomUser
from django.http import HttpResponseRedirect


AVATAR_SIZE = (100, 100)


def get_filtered_name(name):
    """
    Make random file name with allowed extension.
    If extension isn't allowed then it'll return None

    name: str File name
    """

    filename_parts = name.split('.')
    if len(filename_parts) <= 1:
        return None

    ext = filename_parts[-1]
    if ext not in ['jpg', 'png', 'jpeg', 'py']:
        return None

    new_filename = str(uuid.uuid4())[:8]
    return ''.join([new_filename, '.', ext])


def resize_uploaded_image(buf):
    image = Image.open(buf)
    w, h = image.size
    if w < AVATAR_SIZE[0] and h < AVATAR_SIZE[1]:
        resizedImage = image
    else:
        offset_lx = 0
        offset_rx = w
        offset_ly = 0
        offset_ry = h
        if w > h:
            offset_lx = (w - h) / 2
            offset_rx = h / 2 + w / 2
        elif w < h: 
            offset_ly = (h - w) / 2
            offset_ry = w / 2 + h / 2
        print (offset_lx, offset_ly, offset_rx, offset_ry)
        image = image.crop((offset_lx, offset_ly, offset_rx, offset_ry))
        image = image.resize(AVATAR_SIZE)
    resizedImageFile = StringIO.StringIO()
    image.save(resizedImageFile, 'PNG', optimize = True)
    resizedImageFile.seek(0)    # So that the next read starts at the beginning

    return resizedImageFile


def rewrite_url(url):
    """
    Rewrite gcloud public url to proxy url
    """
    return settings.HOST + settings.GCS_MEDIA_URL + url.split('/enggeo')[-1]


@require_http_methods(["POST"])
def upload(request):
    f = request.FILES.get('material', None)

    if f is None:
        return JSONResponse({'status': 400, 'message': 'No file'})
    
    url = upload_file(f, f.name, filter=['jpg', 'png', 'jpeg'])

    if url is None:
        return JSONResponse({'status': 400, 'message': 'wrong file'})
    
    Photo.objects.create(url=url)
    return JSONResponse({'status': 200, 'message': 'ok', 'url': url})


@require_http_methods(["POST"])
def upload_avatar(request):
    f = request.FILES.get('material', None)
    if f is None:
        return JSONResponse({'status': 400, 'message': 'wrong file'})
    image = resize_uploaded_image(f)
    url = upload_file(image, f.name, filter=['jpg', 'png', 'jpeg', 'PNG', 'JPEG', 'JPG'])

    if url is None:
        return JSONResponse({'status': 400, 'message': 'wrong file'})

    if request.user.is_authenticated(): 
        custUser = CustomUser.objects.get(userid=request.user)
        custUser.avatar = url
        custUser.save()
#        return JSONResponse({'status': 200, 'message': 'ok', 'url': url})
    return HttpResponseRedirect("/")


@require_http_methods(["POST"])
def upload_material(request):
    jsonstring = (upload(request))
    data = loads(jsonstring.content)
    message = data.get('message', None)
    if message != 'ok':
        return jsonstring

    url = data.get('url', None)
    return url

from json import loads

from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods

from lib.auth.models import CustomUser
from lib.core.utils import upload_file
from lib.core.views import JSONResponse
from lib.photo.models import Photo
from lib.photo.utils import resize_uploaded_image


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
        custUser = CustomUser.objects.get(user=request.user)
        custUser.avatar = url
        custUser.save()
#        return JSONResponse({'status': 200, 'message': 'ok', 'url': url})
    return HttpResponseRedirect("/")  # TODO: json


@require_http_methods(["POST"])
def upload_material(request):
    jsonstring = (upload(request))
    data = loads(jsonstring.content)
    message = data.get('message', None)
    if message != 'ok':
        return jsonstring

    url = data.get('url', None)
    return url

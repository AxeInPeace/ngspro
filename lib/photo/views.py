import uuid

from gcloud import storage

from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from lib.core.views import JSONResponse
from lib.photo.models import Photo


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


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


def rewrite_url(url):
    """
    Rewrite gcloud public url to proxy url
    """
    return settings.HOST + settings.GCS_MEDIA_URL + url.split('/enggeo')[-1]


@require_http_methods(["POST"])
def upload(request):
    f = request.FILES['material']
    client = storage.Client.from_service_account_json(settings.KEYFILE, settings.GCS_PROJECT)  # TODO: rel paths
    bucket = client.get_bucket(settings.GCS_BUCKET)
    name = get_filtered_name(f.name)
    if name is None:
        return JSONResponse({'status': 400, 'message': 'wrong file'})
    blob = bucket.blob(name)
    blob.upload_from_string(f.read())
    blob.make_public()
    Photo.objects.create(url=rewrite_url(blob.public_url))

    return JSONResponse({'status': 200, 'message': 'ok', 'url': rewrite_url(blob.public_url)})

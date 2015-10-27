import uuid
import types

from gcloud import storage

from django.conf import settings

def get_filtered_name(name, filter):
    """
    Make random file name with allowed extension.
    If extension isn't allowed then it'll return None

    name: str File name,
    filter: list of strs or bool func
    """

    filename_parts = name.split('.')
    if len(filename_parts) <= 1:
        return None

    ext = filename_parts[-1]
    
    if isinstance(filter, list) and ext not in filter\
            or isinstance(filter, types.FunctionType) and filter(name):
        return None

    new_filename = str(uuid.uuid4())[:8]
    return ''.join([new_filename, '.', ext])


def rewrite_url(url):
    """
    Rewrite gcloud public url to proxy url
    """
    return settings.HOST + settings.GCS_MEDIA_URL + url.split('/enggeo')[-1]


def upload_file(readable, filename, filter):
    client = storage.Client.from_service_account_json(settings.KEYFILE, settings.GCS_PROJECT) 
    bucket = client.get_bucket(settings.GCS_BUCKET)

    name = get_filtered_name(filename, filter)
    if name is None:
        return None

    blob = bucket.blob(name)
    blob.upload_from_string(readable.read())
    blob.make_public()
    return rewrite_url(blob.public_url)


def dec_to_grad(decimal):
    g = int(decimal)
    tmp = (decimal - g) * 60
    m = int(tmp)
    s = round((tmp - m) * 100, 2)
    return g, m, s


def grad_to_dec(g, m, s):
    return g + (m + s / 100.0) / 60

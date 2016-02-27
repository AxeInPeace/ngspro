import StringIO
import uuid

from PIL import Image

from django.conf import settings

from lib.photo.const import RESIZE_SIZES

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


def resize_img(url, size):
    """
    Only relative urls
    """
    crop = RESIZE_SIZES.get(size, None)
    return '/%s%s' % (crop, url)

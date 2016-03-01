from django import template

from lib.photo.utils import resize_img

register = template.Library()


@register.filter()
def resize(url, crop):
    """Removes all values of arg from the given string"""
    return resize_img(url, crop)

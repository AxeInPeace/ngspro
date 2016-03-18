from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.decorators import available_attrs


def profile_required(function=None):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.usr.is_registered:
                return view_func(request, *args, **kwargs)
            return redirect(reverse('main') + "#login")
        return _wrapped_view
    if function:
        return login_required(decorator(function))
    return login_required(decorator)

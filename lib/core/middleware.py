from lib.auth.models import CustomUser


class AuthMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            request.usr = CustomUser.objects.filter(user=request.user).first()
            request.user.is_registered = lambda x: x.usr.is_registered
        else:
            request.usr = None
            request.user.is_registered = lambda x: False

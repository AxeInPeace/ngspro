from lib.auth.models import CustomUser


class AuthMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated():
            request.usr = CustomUser.objects.filter(user=request.user).first()
        else:
            request.usr = None

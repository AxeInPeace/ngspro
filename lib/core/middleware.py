from lib.auth.models import CustomUser


class AuthMiddleware(object):
    def process_request(self, request):
        request.usr = CustomUser.objects.filter(userid=request.user).first()

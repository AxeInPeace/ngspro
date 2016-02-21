from django.core.mail import send_mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_mail('test email', 'hello world', 'admin@enggeo.ru',['check-auth@verifier.port25.com'])

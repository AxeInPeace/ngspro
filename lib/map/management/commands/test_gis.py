from django.core.management import BaseCommand

from lib.map.models import Polygon


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Polygon(content_type_id=23, object_id=22, coords='POLYGON(( 55.9552 35.1563, 55.9552 40.078110, 56.3476 40.078110, 56.3476 35.1563, 55.9552 35.1563 ))').save()
        print(Polygon.objects.filter(coords__contains='POINT(56.0000 35.2563)'))
from django.core.management import BaseCommand

from authapp.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.filter(username='admin').first()
        if not user:
            User.objects.create_superuser(username='admin', password='admin', email='admin@mail.ru')
from django.core.management import BaseCommand, call_command
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        call_command('loaddata', 'initial_data')
        for user in User.objects.all():
            user.set_password(user.password)
            user.save()


from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = 'Sets up the database and creates a superuser'

    def handle(self, *args, **options):
        self.create_env()
        call_command('makemigrations')
        call_command('migrate')
        call_command('createsuperuser')

    def create_env(self):
        with open(".env_example", "r") as f:
            data = f.read()

        data = data.replace("SuperSecret", get_random_secret_key())

        with open(".env", "w") as f:
            f.write(data)

from django.core.management import BaseCommand, call_command

class Command(BaseCommand):
    help = (
        'Это моя тестовая команда\n'
        '--locale=ru -- no-location'
    )

    def handle(self, *args: Any, **options: Any):
        call_command('makemassages', '--locale=ru', '--ignore=env', '--no-location')
        return super().handle(*args, **options)
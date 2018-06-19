from django.core.management.base import BaseCommand

from django_uwsgi import uwsgi


class Command(BaseCommand):
    help = "Reloads uWSGI application of the project."

    def handle(self, *args, **options):
        if uwsgi is not None and uwsgi.masterpid() > 0:
            uwsgi.reload()
            print('uWSGI reloaded!')
        else:
            print('The uWSGI master process is not active')

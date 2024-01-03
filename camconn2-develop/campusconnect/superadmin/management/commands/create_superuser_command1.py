import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_none_exists --user=admin --password=changeme
    """

    help = 'Crate a superuser, and allow password to be provided'

    def add_arguments(self, parser):
        parser.add_argument(
            "--username", 
            required=True, 
            default=os.environ.get('DJANGO_SUPERUSER_USERNAME')
        )
        parser.add_argument(
            "--password", 
            required=True, 
            default=os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        )
        parser.add_argument(
            "--email", 
            default=os.environ.get('DJANGO_SUPERUSER_EMAIL')
        )

    def handle(self, *args, **options):

        User = get_user_model()
        if User.objects.exists():
            return

        username = options["username"]
        password = options["password"]
        email = options["email"]

        User.objects.create_superuser(
            username=username, 
            password=password, 
            email=email,
            is_staff=True,
            is_active=True,
            is_superuser=True

        )

        # self.stdout.write(f'user "{username}" was created')
        self.stdout.write("superuser created successfully with username>>>{}".format(username))



# from decouple import config
# from django.db import IntegrityError

### getting name,email & password from env variables
# DJANGO_SU_NAME = os.environ.get('DJANGO_SUPERUSER_USERNAME')
# DJANGO_SU_EMAIL = os.environ.get('DJANGO_SUPERUSER_EMAIL')
# DJANGO_SU_PASSWORD = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

# try:
#     superuser = User.objects.create_superuser(
#         username=DJANGO_SU_NAME,
#         email=DJANGO_SU_EMAIL,
#         password=DJANGO_SU_PASSWORD)
#     superuser.save()
# except IntegrityError:
#     print(f"Super User with username {DJANGO_SU_NAME} is already present")
# except Exception as e:
#     print(e)




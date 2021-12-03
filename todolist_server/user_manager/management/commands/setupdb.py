import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from api.models import ApplicationUser, Category


class Command(BaseCommand):
    help = '''Initializes the database with the required Objects.\n
              usage: setupdb <username> <password> <email> <firstname> <lastname>'''

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The superusers username. Default is root.', default='root')
        parser.add_argument('password', type=str, help='The superusers password.')
        parser.add_argument('email', type=str, help='The superusers email address.')
        parser.add_argument('firstname', type=str, help='The superusers first name.')
        parser.add_argument('lastname', type=str, help='The superusers last name.')

    def handle(self, *args, **options):
        # create new superuser
        adminuser = User.objects.create_superuser(
            username=options['username'],
            password=options['password'],
            email=options['email'],
            first_name=options['firstname'],
            last_name=options['lastname']
        )

        # create associated application user
        appuser = ApplicationUser.objects.create(auth_user=adminuser)

        # create default category
        Category.objects.create(title='Default', color='#26a69a', created_by=appuser)

        print('Initial database setup successful.')

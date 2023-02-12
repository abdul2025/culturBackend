from django.core.management.base import BaseCommand, CommandError
import json
from django.contrib.auth.models import Group



class Command(BaseCommand):
    help = 'Import settings from a json file.'

    def add_arguments(self, parser):
        parser.add_argument('settings_dir', nargs='+', type=str)

    def handle_groups(self, data):
        created_counter = 0
        counter = 0
        for instance in data:
            new_group, created = Group.objects.get_or_create(
                name=instance['name'],
            )
            if created:
                created_counter += 1
                new_group.name = instance['name']
                new_group.save()
            else:
                counter += 1
        return created_counter, counter


    def handle(self, *args, **options):
        try:
            settings_dir = options['settings_dir'][0]
        except:
            raise CommandError(
                'Please pass the directory name of a json file.' )
        f = open(settings_dir)
        data = json.load(f)
        users_updates, total_users = self.handle_groups(data.get('groups'))

        users_updated_groups_output = '\n{}/{} USERS GROUPS CHANGED\n'.format(
            users_updates,
            total_users
        )



        result =users_updated_groups_output
        self.stdout.write(self.style.SUCCESS(result))

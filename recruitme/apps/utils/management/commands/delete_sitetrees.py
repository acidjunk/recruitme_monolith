from django.core.management.base import BaseCommand
from sitetree.models import Tree
from django.core.cache import cache

class Command(BaseCommand):
    args = ''
    help = 'Will delete the sitetree so it can be repopulated. This eases automated deployment.'

    def delete_sitetrees(self):
        Tree.objects.all().delete()
        self.stdout.write('Deleted all sitetrees')
        cache.clear()
        self.stdout.write('Cleared site cache')

        self.stdout.write('''
        Warning
        *****************************************
        * A webserver reload could be needed.   *
        * So reload it manually                 *
        *****************************************
        ''')


    def handle(self, *args, **options):
        self.delete_sitetrees()

from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add cars to the database from fixture'

    def handle(self, *args, **options):

        # Удаляем существующие записи
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Остальной код команды
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

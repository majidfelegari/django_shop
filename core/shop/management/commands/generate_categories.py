from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import ProductCategoryModel
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'generate fake categories'

    def handle(self, *args, **options):
        fake = Faker(locale="fa_IR")

        for _ in range(10):
            title = fake.word()
            slug = slugify(title, allow_unicode=True)
            ProductCategoryModel.objects.get_or_create(title = title, slug=slug)

        self.stdout.write(self.style.SUCCESS('successfully generated 10 fake categories'))
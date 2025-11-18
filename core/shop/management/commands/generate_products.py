from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import ProductModel, ProductCategoryModel,ProductStatusType
from django.utils.text import slugify
from accounts.models import User, UserType
from pathlib import Path
from django.core.files import File
import random

BASE_DIR = Path(__file__).resolve().parent


class Command(BaseCommand):
    help = 'generate fake products'

    def handle(self, *args, **options):
        fake = Faker()
        user = User.objects.get(type=UserType.superuser.value)
        #list image
        image_list = [
            "./images/img1.jpg",
            "./images/img2.jpg",
            "./images/img3.jpg",
            "./images/img4.jpg",
            "./images/img5.jpg",
            "./images/img6.jpg",
            "./images/img7.jpg",
            "./images/img8.jpg",
        ]

        categories = ProductCategoryModel.objects.all()

        for _ in range(10):
            user = user
            num_categories = random.randint(1,4)
            selected_categories = random.sample(list(categories), num_categories)
            title = fake.word()
            slug = slugify(title, allow_unicode=True)
            selected_image = random.choice(image_list)
            image_obj = File(file=open(BASE_DIR / selected_image,"rb"), name=Path(selected_image).name)
            description = fake.text()
            stock = fake.random_int(min=0, max=10)
            status = random.choice(ProductStatusType.choices)[0]
            price = fake.random_int(min=10000,max=100000)
            discount_percent = fake.random_int(min=0, max=50)

            product = ProductModel.objects.create(
                user = user,
                title = title,
                slug= slug,
                image = image_obj,
                description = description,
                stock = stock,
                status = status,
                price = price,
                discount_percent = discount_percent,
            )
            product.category.set(selected_categories)

        self.stdout.write(self.style.SUCCESS('successfully generated 10 fake products'))



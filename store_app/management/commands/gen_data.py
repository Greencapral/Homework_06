from django.core.management import BaseCommand
from faker import Faker
from random import randint, choice

from store_app.models import Product, Category


class Command(BaseCommand):
    help = "Генерация тестовых данных для моделей Product и Category"

    def handle(self, *args, **kwargs):
        self.stdout.write("Генерируем категории")
        cat_names = [
            "Продукты питания",
            "Бытовая химия",
            "Товары для дома",
            "Электроника и бытовая техника",
            "Одежда и аксессуары",
            "Спорт и активный отдых",
        ]

        fake = Faker()

        categories = []
        for _ in range(6):
            category = Category.objects.create(
                name=cat_names[_]
            )
            categories.append(category)

        self.stdout.write("Генерируем товары")

        products = []
        for _ in range(20):
            product = Product.objects.create(
                name=" ".join(fake.words(nb=2)),
                price=fake.random_number(randint(1, 3)),
                category=choice(categories),
                description=fake.text(max_nb_chars=150),
            )
            products.append(product)

        self.stdout.write("Генерация закончена")

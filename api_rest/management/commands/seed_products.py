from django.core.management.base import BaseCommand
from api_rest.models import Products

class Command(BaseCommand):
    help = 'Seed products into the database'

    def handle(self, *args, **kwargs):
        products = [
            {
                "name": "Celular 1",
                "price": 1800.00,
                "description": "Lorenzo Ipsulum"
            },
            {
                "name": "Celular 2",
                "price": 3200.00,
                "description": "Lorem ipsum dolor"
            },
            {
                "name": "Celular 3",
                "price": 9800.00,
                "description": "Lorem ipsum dolor sit amet"
            },
        ]

        for product in products:
            Products.objects.create(**product)
            self.stdout.write(self.style.SUCCESS(f'Successfully added {product["name"]}'))

        self.stdout.write(self.style.SUCCESS('All products have been seeded!'))

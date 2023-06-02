import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoplocator.settings')
django.setup()

from faker import Faker
from random import randint, uniform
from shop.models import Shop

faker = Faker()

def populate_shops(n):
    for _ in range(n):
        name = faker.company()
        latitude = uniform(-90, 90)
        longitude = uniform(-180, 180)
        shop = Shop.objects.create(name=name, latitude=latitude, longitude=longitude)
        shop.save()

populate_shops(100)

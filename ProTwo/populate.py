import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()


def populate(N=10):

    for entry in range(N):
        fake_first,fake_last = fakegen.name().split()
        fake_email = fakegen.free_email()
        usr = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)

if __name__=='__main__':
    print('Populating Script')
    populate(20)
    print("Populating Complete")

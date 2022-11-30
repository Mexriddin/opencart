import random
from opencart.tools.data.datas import User
from faker import Faker

faker_en = Faker('En')


def generated_user():
    return User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        phone=faker_en.msisdn(),
        password=faker_en.msisdn()
    )
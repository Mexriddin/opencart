import random
from opencart.tools.data.datas import User, Product
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


def generated_product():
    return Product(
        product_name="product_test_name:" + faker_en.name(),
        product_tag="test_tag",
        product_model="test_model"
    )



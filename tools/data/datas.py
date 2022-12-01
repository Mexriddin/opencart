from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    password: str = None


@dataclass
class Product:
    product_name: str = None
    product_tag: str = None
    product_model: str = None

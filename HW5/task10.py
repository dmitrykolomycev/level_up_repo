"""products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone Case", "price": 30},
    {"name": "Phone", "price": 600},
]
# Функция фильтрации
def is_phone(product):
    return "Phone" in product["name"]
# Используем filter для оставления только нужных товаров
phones = list(filter(is_phone, products))
print(phones)"""
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone Case", "price": 30},
    {"name": "Phone", "price": 600},
]

def is_phone(product):
    return "Phone" in product["name"]

phones = list(filter(is_phone, products))

print(phones)
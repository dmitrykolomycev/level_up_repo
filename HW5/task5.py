"""У вас есть список цен и категория, к которой нужно применить скидку. Напишите функцию, которая с помощью map применяет скидку 10% к заданным категориям.
# Задача
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 50, "category": "clothing"},
    {"name": "Phone", "price": 600, "category": "electronics"},
]

def apply_discount(product):
    # Если категория electronics, примените скидку 10%
    pass

discounted_products = None  # Используйте map
print(discounted_products)
# Ожидаемый результат:
# [{"name": "Laptop", "price": 900.0, "category": "electronics"},
#  {"name": "Shirt", "price": 50, "category": "clothing"},
#  {"name": "Phone", "price": 540.0, "category": "electronics"}]"""
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 50, "category": "clothing"},
    {"name": "Phone", "price": 600, "category": "electronics"},
]

def apply_discount(product):
    if product["category"] == "electronics":
        product["price"] *= 0.9
    return product

discounted_products = list(map(apply_discount, products))
print(discounted_products)
for product in products:
   print(product)




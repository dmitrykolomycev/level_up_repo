"""Удаление товаров с низким рейтингом через filter
Фильтруйте товары с рейтингом меньше 4.
# Задача
products = [
    {"name": "Laptop", "rating": 4.5},
    {"name": "Shirt", "rating": 3.8},
    {"name": "Phone", "rating": 4.2},
]
# Используйте filter для удаления товаров с рейтингом < 4
high_rating_products = None
print(high_rating_products)
# Ожидаемый результат: [{"name": "Laptop", "rating": 4.5}, {"name": "Phone", "rating": 4.2}]"""

products = [
    {"name": "Laptop", "rating": 4.5},
    {"name": "Shirt", "rating": 3.8},
    {"name": "Phone", "rating": 4.2},
]
high_rating_products = list(filter(lambda x: x["rating"] >= 4, products))

print(high_rating_products)
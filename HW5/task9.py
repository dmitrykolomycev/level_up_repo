"""Генерация строк описания товаров через map
Создайте список строк описания для каждого товара вида: "Товар: , Цена: ".
# Задача
products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Shirt", "price": 50},
    {"name": "Phone", "price": 600},
]
def format_product(product):
    # Верните строку вида: "Товар: <name>, Цена: <price>"
    pass
descriptions = None  # Используйте map
print(descriptions)
# Ожидаемый результат: ["Товар: Laptop, Цена: 1000", "Товар: Shirt, Цена: 50", "Товар: Phone, Цена: 600"]"""

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Shirt", "price": 50},
    {"name": "Phone", "price": 600},
]
def format_product(product):
    return f"Товар: {product['name']}, Цена: {product['price']}"

descriptions = list(map(format_product, products))

print(descriptions)

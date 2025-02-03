"""Есть глобальная переменная с базовой ценой товара. Напишите функцию, которая временно изменяет цену локально.
# Задача
base_price = 100

def apply_discount(discount):
    # Локально измените базовую цену, применив скидку
    new_price = None  # Локально посчитайте цену со скидкой
    print(f"Цена со скидкой: {new_price}")

apply_discount(20)  # Цена со скидкой: 80
print(base_price)   # Ожидаемый результат: 100"""

base_price = 100

def apply_discount(discount):
    new_price = base_price - discount
    print(f"Цена со скидкой: {new_price}")

apply_discount(20)
print(base_price)
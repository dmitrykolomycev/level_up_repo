"""Список цен товаров. Напишите функцию, которая добавляет к каждому товару налог 20%, и примените её с помощью map.
# Задача
prices = [100, 200, 300, 400]

def apply_tax(price):
    # Верните цену с налогом 20%
    pass

final_prices = None  # Используйте map для применения функции apply_tax
print(final_prices)  # Ожидаемый результат: [120.0, 240.0, 360.0, 480.0]"""

prices = [100, 200, 300, 400]

def apply_tax(price):
    return price * 1.2

final_prices = list(map(apply_tax, prices))
print(final_prices)
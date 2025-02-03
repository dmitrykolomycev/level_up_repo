""" Перевод в рубли через map
Есть список цен в долларах. Напишите функцию, которая переводит их в рубли (курс 1 USD = 75 RUB), и примените через map.
# Задача
prices_usd = [10, 20, 30, 40]

def to_rub(price):
    # Переведите цену в рубли
    pass

prices_rub = None  # Используйте map для преобразования
print(prices_rub)  # Ожидаемый результат: [750, 1500, 2250, 3000] """

prices_usd = [10, 20, 30, 40]

def to_rub(price):
    return price * 75

prices_rub = list(map(to_rub, prices_usd))

print(prices_rub)
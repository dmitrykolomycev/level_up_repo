''' Фильтрация параметров через **kwargs
Напишите функцию, которая принимает параметры через **kwargs и возвращает только те, где значение больше 10.
# Задача
def filter_kwargs(**kwargs):
    # Верните словарь с ключами, где значение больше 10
    pass

result = filter_kwargs(a=5, b=15, c=25, d=8)
print(result)  # Ожидаемый результат: {'b': 15, 'c': 25}
'''

def filter_kwargs(**kwargs):
    filtered = {key: value for key, value in kwargs.items() if value > 10}
    return filtered

result = filter_kwargs(a=5, b=15, c=25, d=8)
print(result)

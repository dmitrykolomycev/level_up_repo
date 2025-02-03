"""Создание словаря из ключей и значений (**kwargs)
Напишите функцию, которая принимает произвольное количество именованных аргументов и возвращает их в виде словаря.
# Задача
def create_dict(**kwargs):
    # Верните kwargs как словарь
    pass
result = create_dict(name="Alice", age=25, city="New York")
print(result)  # Ожидаемый результат: {'name': 'Alice', 'age': 25, 'city': 'New York'}
"""

def create_dict(**kwargs):
    return kwargs
result = create_dict(name="Alice", age=25, city="New York")
print(result)
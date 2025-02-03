"""Сложение чисел и ключевых параметров
Напишите функцию, которая принимает числовые аргументы через *args и добавляет к их сумме значения из **kwargs, если они являются числами.
# Задача
def sum_args_kwargs(*args, **kwargs):
    # Сложите числа из args и числовые значения из kwargs
    pass
result = sum_args_kwargs(1, 2, 3, x=4, y=5, z="не число")
print(result)  # Ожидаемый результат: 15
"""

def sum_args_kwargs(*args, **kwargs):
    total = sum(args)
    for value in kwargs.values():
        if isinstance(value, (int, float)):  # Проверяем, является ли значение числом
            total += value
    return total
result = sum_args_kwargs(1, 2, 3, x=4, y=5, z="не число")
print(result)
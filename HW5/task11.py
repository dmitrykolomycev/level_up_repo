"""Сумма произвольного количества чисел (*args)
Напишите функцию, которая принимает произвольное количество чисел и возвращает их сумму.
# Задача
def sum_numbers(*args):
    # Верните сумму всех переданных чисел
    pass

result = sum_numbers(1, 2, 3, 4, 5)
print(result)  # Ожидаемый результат: 15"""

def sum_numbers(*args):
    return sum(args)

result = sum_numbers(1, 2, 3, 4, 5)
print(result)

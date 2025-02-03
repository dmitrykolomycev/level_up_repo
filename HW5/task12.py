"""
Наибольшее число из *args
Напишите функцию, которая принимает произвольное количество чисел и возвращает наибольшее из них.
# Задача
def max_number(*args):
    # Верните наибольшее число
    pass
result = max_number(10, 25, 50, 5, 30)
print(result)  # Ожидаемый результат: 50
"""

def max_number(*args):

    return max(args)

result = max_number(10, 25, 50, 5, 30)
print(result)




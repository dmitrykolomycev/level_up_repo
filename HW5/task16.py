"""Объединение списков через *args
Напишите функцию, которая принимает произвольное количество списков и возвращает их объединение в один список.
# Задача
def merge_lists(*args):
    # Объедините все переданные списки
    pass
result = merge_lists([1, 2], [3, 4], [5, 6])
print(result)  # Ожидаемый результат: [1, 2, 3, 4, 5, 6]
"""

def merge_lists(*args):
    merged_list = []
    for lst in args:
        merged_list.extend(lst)
    return merged_list

result = merge_lists([1, 2], [3, 4], [5, 6])
print(result)
""". Отбор участников старше 18 лет
У вас есть список участников с возрастом. Используйте filter, чтобы оставить только тех, кто старше 18 лет.
# Задача
participants = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "Diana", "age": 22},
]
# Используйте filter для отбора участников старше 18 лет
adults = None
print(adults)
# Ожидаемый результат: [{"name": "Bob", "age": 20}, {"name": "Diana", "age": 22}]
"""

participants = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "Diana", "age": 22},
]
def is_adult(participant):
    return participant["age"] > 18

adults = list(filter(is_adult, participants))

print(adults)
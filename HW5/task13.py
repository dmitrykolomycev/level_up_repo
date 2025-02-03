"""Приветствие произвольного количества людей (*args)
Напишите функцию, которая принимает список имен и приветствует каждого из них.
# Задача
def greet_people(*args):
    # Для каждого имени выведите "Привет, <имя>!"
    pass
greet_people("Alice", "Bob", "Charlie")
# Ожидаемый результат:
# Привет, Alice!
# Привет, Bob!
# Привет, Charlie!
"""

def greet_people(*args):

    for name in args:
        print(f"Привет, {name}!")

greet_people("Alice", "Bob", "Charlie")
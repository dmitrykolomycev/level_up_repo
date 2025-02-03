"""Программа отслеживает общее количество клиентов. Напишите функцию, которая увеличивает глобальный счётчик клиентов.
# Задача
clients = 0

def add_client():
    # Увеличьте значение глобальной переменной clients на 1
    pass

add_client()
add_client()
print(clients)  # Ожидаемый результат: 2
"""

clients = 0

def add_client():
    global clients
    clients += 1


add_client()
add_client()
print(clients)
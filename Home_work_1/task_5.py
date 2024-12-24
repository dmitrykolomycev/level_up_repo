"""Программа запрашивает координаты точки (x,y) и определяет, в какой четверти декартовой плоскости она находится."""
import random  


name = input("Введите, пожалуйста, Ваше имя: ")

if random.choice([True, False]):
    name = name.upper()
else: 
    name = name.lower()

print(name)    
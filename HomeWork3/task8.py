"""Задача 8: Выберите случайное поздравление из списка, не включая те, которые содержат слово "скучный". Подсказка в задаче 3.
# Решение
greetings = ["С днём рождения!", "С Новым годом!", "Желаю успехов!", "Скучный текст"]
"""
import random

greetings = ["С днём рождения!", "С Новым годом!", "Желаю успехов!", "Скучный текст"]

filter = [f for f in greetings if "Скучный" not in f]


congratilations = random.choice(filter)

print(congratilations)

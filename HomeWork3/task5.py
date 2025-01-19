"""Задача: Сгенерируйте пароль из случайного набора символов длиной 8. Подсказка в 3 задаче.
# Решение
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
"""

import random
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
letter_1 = random.choice(letters)
letter_2 = random.choice(letters)
letter_3 = random.choice(letters)
letter_4 = random.choice(letters)
letter_5 = random.choice(letters)
letter_6 = random.choice(letters)
letter_7 = random.choice(letters)
letter_8 = random.choice(letters)


recept = []
recept.extend([letter_1, letter_2, letter_3, letter_4, letter_5, letter_6, letter_7, letter_8])
print("".join(recept))
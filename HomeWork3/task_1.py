"""Дано число n. Создайте список от n до 0."""

n = int(input("Введите число: "))
if n < 0:
    spisok = list(range(n, 1))
    print(spisok)
elif n > 0:
    spisok = list(range(n,  -1, -1))
    print(spisok)
else:
    print("Введите число не равное 0.")

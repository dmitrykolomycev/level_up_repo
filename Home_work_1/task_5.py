"""Программа запрашивает координаты точки (x,y) и определяет, в какой четверти декартовой плоскости она находится."""
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Определение четверти
if x > 0:
    if y > 0:
        print("Точка находится в первой четверти.")
    else:
        print("Точка находится в четвертой четверти.")
elif x < 0:
    if y > 0:
        print("Точка находится во второй четверти.")
    else:
        print("Точка находится в третьей четверти.")
else:
    if y != 0:
        print("Точка находится на оси Y.")
    else:
        print("Точка находится в начале координат.")

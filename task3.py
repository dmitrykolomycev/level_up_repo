number = 5 #int(input("Введите число: "))

# Списковое выражение для умножения и вывода
print(*[f"{number} * {i} = {number * i}" for i in range(11)], sep="\n")

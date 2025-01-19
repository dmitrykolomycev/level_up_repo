"""У вас есть список чисел. Разделите его на два списка: чётные и нечётные числа.
# Решение
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []   #четные
odd_numbers = []    #нечетные

for numb in numbers:
    if numb % 2 == 0:
        even_numbers.append(numb)
    else:
      odd_numbers.append(numb)

print(f"Четные числа: " + ", ".join(map(str, even_numbers)) + ".")

print(f"Четные числа: " + ", ".join(map(str, odd_numbers)) + ".")
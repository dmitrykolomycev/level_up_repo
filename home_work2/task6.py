"""Задача: Напишите программу, которая запрашивает у пользователя число и проверяет, является ли оно простым.
 Число называется простым, если оно делится только на 1 и на само себя.
 Используйте цикл for для проверки делимости."""
number = int(input("Введите число, а программа определит простое оно или нет: "))

if number < 2:
    print(f"{number} не является простым числом.")
else:
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(str(number) + " является простым числом.")
    else:
        print(str(number) + " не является простым числом.")


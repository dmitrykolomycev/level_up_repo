number = int(input("Введите число, а программа определит простое оно или нет: "))

if number < 2:
    print(f"{number} не является простым числом.")
else:
    prostoe = all(number % i != 0 for i in range(2, int(number**0.5) + 1))

    if prostoe:
        print(str(number) + " является простым числом.")
    else:
        print(str(number) + " не является простым числом.")
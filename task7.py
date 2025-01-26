

number = int(input("Введите число, программа посчитает его факториал: "))

if number == 0: # проверка, если введено 0
    factorial = 1
    print("Факториал для 0 равен = " + str(factorial) + ".")
elif number < 0: # проверка, если введено отрицательное число
    print("Факториал числа n — это произведение всех натуральных (натуральные числа не могут быть отрицательными) чисел от единицы до n.")
else:
    factorial = 1 if number == 0 else eval('*'.join(str(i) for i in range(1, number + 1)))
    print("Факториал введенного вами числа: " + str(number) + ", равен = " + str(factorial) + ".")
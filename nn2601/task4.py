number = int(input("Введите число: "))

summa = sum([i for i in range(1, number + 1) if i % 2 == 0])
print("Cумма всех четных чисел от 1 до введеного вами числа: " + str(number) + ", равна = " + str(summa))


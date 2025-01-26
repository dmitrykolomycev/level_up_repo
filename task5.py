
number = int(input("Введите число: "))

summa = sum([i for i in range(1, number + 1) if i % 3 == 0])
print("Cумма всех  чисел от 1 до введеного вами числа и делящихся без остатка на 3: " + str(number) + ", равна = " + str(summa))


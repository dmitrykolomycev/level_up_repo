number = int(input("Введите число: "))
summa = 0
i = 0
while i <= (number):
    i = i + 1
    if i % 3 == 0:
        summa = summa + i

print("Cумма всех чисел, делящихся без остатака на 3,  от 1 до введеного вами числа: " + str(number) + ", равна  =  " + str(summa))

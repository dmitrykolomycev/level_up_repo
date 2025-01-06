number = int(input("Введите число: "))
summa = 0

for i in range(1, number +1 ):
    if i % 2 == 0:
        summa = summa + i

print("Cумма всех четных чисел от 1 до введеного вами числа: " + str(number) + ", равна  =  " + str(summa))

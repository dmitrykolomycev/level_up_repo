"""Напишите программу, которая запрашивает у пользователя строку и проверяет,
является ли она палиндромом (читается одинаково слева направо и справа налево).
Пробелы и регистр букв не учитываются."""


word = input("Введите строку, а программа  проверит палиндромом или нет: ")
word = word.lower()
word = word.replace(' ', '')
print(word)
check_pall = ""
l = len(word)
for i in range(l - 1, -1, -1):
    check_pall = check_pall + word[i]
print(check_pall)

if word == check_pall:
    print("Введенное строка это паллидром: " + check_pall + ".")
else:
    print("Введенное строка это НЕ паллидром: " + word + ".")
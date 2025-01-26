word = input("Введите строку, а программа проверит палиндромом или нет: ")
word = word.lower().replace(' ', '')

check_pall = ''.join([word[i] for i in range(len(word) - 1, -1, -1)])

if word == check_pall:
    print(f"Введенная строка это палиндром: {check_pall}.")
else:
    print(f"Введенная строка это НЕ палиндром: {word}.")
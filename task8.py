word = input("Введите строку, а программа выведет ее в обратном порядке: ")

reversed_word = ''.join([word[i] for i in range(len(word) - 1, -1, -1)])

print(reversed_word)


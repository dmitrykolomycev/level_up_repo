"""Задача 2: "Сравнение длины слов"
Программа запрашивает два слова и сравнивает их длину. Если длина одинаковая, выводит: "Слова одинаковой длины", 
иначе указывает, какое слово длиннее. 
Hint: Самостоятельно найдите как на питоне ищется длина объектов
"""

first_word = input("Введите ваше первое  слово: ")
second_word = input("Введите ваше второе слово: ")

if len(first_word) > len(second_word):
  print("Первое слово длинее: " + first_word + ".")
elif len(first_word) < len(second_word):
  print("Второе слово длинее: " + second_word + ".")
else:
  print("Слова одинаковой длины.")

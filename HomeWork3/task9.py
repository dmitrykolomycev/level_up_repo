"""Задача 9: Замените все неприличные слова в тексте звездочками.
# Решение
text = "Эта программа такая тупая! Вот блин!"
bad_words = ["тупая", "блин"]"""

text = "Эта программа такая тупая! Вот блин!"
bad_words = ["тупая", "блин"]

for word  in bad_words:
    text = text.replace(word, '*' * len(word))

print(text)


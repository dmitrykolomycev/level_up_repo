"""Программа просит ввести имя и случайно выбирает, в каком регистре его вывести: верхнем или нижнем."""
name = input("Введите, пожалуйста, Ваше имя: ")

if random.choice([True, False]):
    name = name.upper()
else: 
    name = name.lower()

print(name)    

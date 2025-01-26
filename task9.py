import random

number = random.randint(1, 100)

print("Программа загадала число от 1 до 100. Попробуйте угадать его!")  # приветствие вне цикла

while True:  # бесконечный цикл, пока пользователь не угадает
    number_user = int(input("Введите ваше число: "))

    message = [
        f"Поздравляю, вы угадали!!! Загаданное число: {number}" if number_user == number else None,
        "Горячо!" if abs(number - number_user) <= 10 else None,
        "Больше!" if number > number_user else None,
        "Меньше!" if number < number_user else None
    ]

    response = next((resp for resp in message if resp is not None), None)
    
    if response:
        print(message)
    
    if number_user == number:
        break  # выходим из цикла, когда угадали
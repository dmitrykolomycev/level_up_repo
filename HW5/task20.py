"""Проверка ключевых аргументов (**kwargs)
Напишите функцию, которая проверяет наличие ключа required в **kwargs и возвращает его значение. Если ключа нет, возвращает "Ключ не найден".
# Задача
def check_required(**kwargs):
    # Проверьте наличие ключа required
    pass
result1 = check_required(required="Это важно", optional="Это не важно")
result2 = check_required(optional="Это не важно")
print(result1)  # Ожидаемый результат: "Это важно"
print(result2)  # Ожидаемый результат: "Ключ не найден"
"""

def check_required(**kwargs):
    if 'required' in kwargs:
        return kwargs['required']
    else:
        return "Ключ не найден"

result1 = check_required(required="Это важно", optional="Это не важно")
result2 = check_required(optional="Это не важно")
print(result1)
print(result2)

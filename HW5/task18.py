"""Комбинация *args и **kwargs
Напишите функцию, которая принимает список имен через *args и сообщения через **kwargs, чтобы отправить каждому сообщение.
# Задача
def send_messages(*args, **kwargs):
    # Для каждого имени выведите сообщение вида:
    # "Привет, <имя>! <сообщение>"
    # Используйте значение kwargs['message']
    pass

send_messages("Alice", "Bob", message="У вас новое уведомление!")
# Ожидаемый результат:
# Привет, Alice! У вас новое уведомление!
# Привет, Bob! У вас новое уведомление!
"""

def send_messages(*args, **kwargs):
    message = kwargs.get('message', 'Нет сообщения')
    for name in args:
        print(f"Привет, {name}! {message}")

send_messages("Alice", "Bob", message="У вас новое уведомление!")
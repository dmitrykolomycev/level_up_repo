"""Форматирование текста с помощью **kwargs
Напишите функцию, которая принимает текстовый шаблон и подставляет значения из **kwargs.
# Задача
def format_text(template, **kwargs):
    # Используйте .format() для подстановки значений из kwargs
    pass
result = format_text("Привет, {name}! Ты живешь в {city}.", name="Alice", city="New York")
print(result)  # Ожидаемый результат: "Привет, Alice! Ты живешь в New York."
"""

def format_text(template, **kwargs):
    return template.format(**kwargs)

result = format_text("Привет, {name}! Ты живешь в {city}.", name="Alice", city="New York")
print(result) 
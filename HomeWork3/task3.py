"""Задача: У вас есть список ингредиентов. Напишите программу, которая случайно выберет три ингредиента для нового рецепта. Изучите как работает random.choice() самостоятельно
import random
# Решение
ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]"""
import random
ingredients = ["сыр", "яйца", "помидоры", "курица", "рыба", "грибы", "лук"]
ingr_1 = random.choice(ingredients)
ingr_2 = random.choice(ingredients)
ingr_3 = random.choice(ingredients)

recept = []
recept.extend([ingr_1, ingr_2, ingr_3])
print(recept)
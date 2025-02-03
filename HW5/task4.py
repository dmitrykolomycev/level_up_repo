"""Есть список цен. Используйте filter, чтобы оставить только товары дороже 150
prices = [50, 120, 180, 300, 75]
# Используйте filter, чтобы отобрать только товары дороже 150
expensive_items = None
print(expensive_items)  # Ожидаемый результат: [180, 300]
"""

prices = [50, 120, 180, 300, 75]
expensive_items = list(filter(lambda price: price > 150, prices))
print(expensive_items) 
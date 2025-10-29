# ===== Імпорт бібліотек ===== 
import requests   # для роботи з веб-запитами
import numpy as np  # для роботи з масивами і математичними операціями
import pandas as pd  # для роботи з таблицями (DataFrame)
import matplotlib.pyplot as plt  # для побудови графіків
import json  # для серіалізації/десеріалізації об'єктів у формат JSON
import math  # математичні функції (sqrt, sin, cos, factorial)
import os  # робота з файлами та ОС
import sys  # доступ до системних параметрів і аргументів
import random  # генерація випадкових чисел
import datetime  # робота з датами та часом

print("Лабораторна №5: Використання бібліотек у Python\n")

# ====== 1. requests ======
try:
    # робимо GET-запит до GitHub API
    response = requests.get("https://api.github.com")
    print("1. requests: Статус відповіді =", response.status_code)
except Exception as e:
    # якщо щось пішло не так (немає Інтернету, неправильний URL)
    print("Помилка в бібліотеці requests:", e)

# ====== 2. numpy ======
try:
    # створюємо масив і обчислюємо середнє
    arr = np.array([1, 2, 3, 4, 5])
    print("2. numpy: середнє значення =", np.mean(arr))
except Exception as e:
    print("Помилка в бібліотеці numpy:", e)

# ====== 3. pandas ======
try:
    # створюємо таблицю з іменами та оцінками
    data = {"Ім'я": ["Аня", "Саша", "Ігор"], "Оцінка": [95, 88, 76]}
    df = pd.DataFrame(data)
    print("3. pandas: таблиця\n", df)
except Exception as e:
    print("Помилка в бібліотеці pandas:", e)

# ====== 4. matplotlib ======
try:
    # будуємо графік і зберігаємо у файл
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("4. matplotlib: приклад графіка")
    plt.savefig("plot.png")
    print("4. matplotlib: графік збережено як plot.png")
except Exception as e:
    print("Помилка в бібліотеці matplotlib:", e)

# ====== 5. json ======
try:
    # перетворюємо словник у JSON-рядок
    obj = {"ім'я": "Саша", "курс": 2, "предмет": "Основи програмування"}
    json_str = json.dumps(obj, ensure_ascii=False, indent=4)
    print("5. json: серіалізація об'єкта\n", json_str)
except Exception as e:
    print("Помилка в бібліотеці json:", e)

# ===== Імпорт бібліотек =====
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import math
import os
import sys
import random
import datetime

print("Лабораторна №5: Використання бібліотек у Python\n")

# ====== 1. requests ======
try:
    response = requests.get("https://api.github.com")
    print("1. requests: Статус відповіді =", response.status_code)
except Exception as e:
    print("Помилка в бібліотеці requests:", e)

# ====== 2. numpy ======
try:
    arr = np.array([1, 2, 3, 4, 5])
    print("2. numpy: середнє значення =", np.mean(arr))
except Exception as e:
    print("Помилка в бібліотеці numpy:", e)

# ====== 3. pandas ======
try:
    data = {"Ім'я": ["Богдана", "Саша", "Ірина"], "Оцінка": [1, 12, 2]}
    df = pd.DataFrame(data)
    print("3. pandas: таблиця\n", df)
except Exception as e:
    print("Помилка в бібліотеці pandas:", e)

# ====== 4. matplotlib ======
try:
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.title("4. matplotlib: приклад графіка")
    plt.savefig("plot.png")
    print("4. matplotlib: графік збережено як plot.png")
except Exception as e:
    print("Помилка в бібліотеці matplotlib:", e)

# ====== 5. json ======
try:
    obj = {"ім'я": "Саша", "курс": 2, "предмет": "Основи програмування"}
    json_str = json.dumps(obj, ensure_ascii=False, indent=4)
    print("5. json: серіалізація об'єкта\n", json_str)
except Exception as e:
    print("Помилка в бібліотеці json:", e)

from decorator import validate_positive

@validate_positive
def multiply(a, b):
    return a * b

@validate_positive
def add_three_numbers(a, b, c):
    return a + b + c

if __name__ == "__main__":
    # Коректний виклик
    print(multiply(3, 5))          # 15
    print(add_three_numbers(2, 4, 8))  # 14

    # Некоректний виклик — один аргумент від'ємний
    try:
        print(multiply(3, -2))
    except ValueError as e:
        print("Помилка:", e)

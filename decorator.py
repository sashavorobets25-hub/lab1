def validate_positive(func):
    def wrapper(*args, **kwargs):
        # Перевіряємо всі аргументи (позиційні й іменовані)
        all_args = list(args) + list(kwargs.values())

        for arg in all_args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Аргумент {arg} не є додатнім числом!")

        return func(*args, **kwargs)
    return wrapper
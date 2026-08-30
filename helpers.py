# helpers.py — вспомогательные функции

import random
import string

def generate_unique_email():
    """
    Генерирует уникальный email в формате:
    имя_фамилия_номер_когорты_три_цифры@yandex.ru
    
    Например: ivan_petrov_5_123@yandex.ru
    """
    # Список имён и фамилий для разнообразия
    first_names = ['ivan', 'petr', 'alex', 'mikhail', 'dmitry', 'sergey', 'andrey']
    last_names = ['ivanov', 'petrov', 'sidorov', 'smirnov', 'kozlov', 'morozov', 'volkov']
    
    # Выбираем случайные имя и фамилию
    name = random.choice(first_names)
    surname = random.choice(last_names)
    
    # Номер когорты (от 1 до 20)
    cohort = random.randint(1, 20)
    
    # Три случайные цифры
    digits = ''.join(random.choices(string.digits, k=3))
    
    # Собираем email
    email = f"{name}_{surname}_{cohort}_{digits}@yandex.ru"
    
    return email

def generate_password():
    """
    Генерирует пароль для тестов.
    Возвращает либо корректный пароль (6+ символов),
    либо некорректный (меньше 6 символов) — для проверки ошибки.
    """
    # Для корректного пароля (6 символов)
    valid_password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    
    # Для некорректного пароля (5 символов)
    invalid_password = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    
    # Возвращаем оба варианта — в тестах будем выбирать
    return valid_password, invalid_password
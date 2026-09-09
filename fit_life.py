# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_PER_L = 1000


# 1. Знакомство
# Спрашиваем у пользователя имя и сохраняем в переменную user_name
# Спрашиваем возраст и сохраняем в переменную user_age
print('Добрый день! Это FitLife.')
user_name = input('Как вас зовут? ')
user_age = int(input('Сколько вам лет? '))


# 2. Сбор данных
# Запрашиваем вес (в кг) и сохраняем в user_weight
# Запрашиваем рост (в метрах, например 1.75) и сохраняем в user_height
user_weight = float(input(
    'Укажите ваш вес в килограммах, '
    'используйте точку в качестве разделителя - например, 61.5 '))
user_height = float(input(
    'Укажите ваш рост в метрах,'
    ' Используйте точку в качестве разделителя - например, 1.75 '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Рассчитываем bmi (Индекс массы тела)
def calculate_bmi(user_weight, user_height):
    """Рассчитываем ИМТ."""
    bmi = user_weight / (user_height ** 2)
    return bmi


# Подсчет воды: вес * 30 мл
def calculate_water(user_weight):
    """Рассчитываем необходимое количество воды в день."""
    water_needed = user_weight * WATER_PER_KG
    return water_needed


# 4. Запись расчетов функций в переменные
# Рассчитываем ИМТ и необходимое количество воды
bmi = calculate_bmi(user_weight, user_height)
water_needed_ml = calculate_water(user_weight)
water_needed_l = water_needed_ml / ML_PER_L


# 5. Вывод красивого результата
# Выводим приветствие
# Указываем возраст, ИМТ и норму воды.
print()
print('=' * 10)
print(
    f'Привет, {user_name}!\n'
    f'Ваш возраст: {user_age}\n'
    f'Ваш ИМТ: {bmi:.1f}\n'
    f'Ваша норма воды: {water_needed_l:.2f} литров в день.\n')
print('Расчет окончен. Будьте здоровы!')

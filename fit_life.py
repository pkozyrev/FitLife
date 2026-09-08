# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_PER_L = 1000


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
print('Добрый день! Это FitLife.')
user_name = input('Как вас зовут? ')
user_age = int(input('Сколько вам лет? '))


# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_weight = float(input('Какой у вас вес в килограммах? Используйте точку в качестве разделителя - например, 61.5 '))
user_height = float(input('Какой у вас рост в метрах? Используйте точку в качестве разделителя - например, 1.75 '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def calculate_bmi(user_weight, user_height):
    """Рассчитываем ИМТ."""
    bmi = user_weight / (user_height ** 2)
    return bmi


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def calculate_water(user_weight):
    """Рассчитываем необходимое количество воды в день."""
    water_needed = user_weight * WATER_PER_KG
    return water_needed


# 4. Запись расчетов в переменные
bmi = calculate_bmi(user_weight, user_height)
water_needed_ml = calculate_water(user_weight)
water_needed_l = water_needed_ml / ML_PER_L


# 5. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print()
print('=' * 10)
print(f'Привет, {user_name}!')
print(f'Ваш возраст: {user_age}\nВаш ИМТ: {bmi:.1f}\nВаша норма воды: {water_needed_l:.2f} литров в день.\n')
print('Расчет окончен. Будьте здоровы!')

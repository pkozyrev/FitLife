# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30
ML_PER_L = 1000


# 1. Знакомство
# Спрашиваем у пользователя имя и сохраняем в переменную user_name
# Спрашиваем возраст и сохраняем в переменную user_age
# добавляем "защиту от дурака при помощи циклов" для каждой переменной
print('Добрый день! Это FitLife.')
user_name = input('Как вас зовут? ').strip()
while not user_name:
    print("Имя не может быть пустым!")
    user_name = input('Как вас зовут? ').strip()

user_age = int(input('Сколько вам лет? '))
while user_age < 0 or user_age > 125:
    print("Возраст не может принимать такие значения!")
    user_age = int(input('Сколько вам лет? '))


# 2. Сбор данных
# Запрашиваем вес (в кг) и сохраняем в user_weight
# Запрашиваем рост (в метрах, например 1.75) и сохраняем в user_height
# добавляем "защиту от дурака при помощи циклов" для каждой переменной
user_weight = float(input(
    'Укажите ваш вес в килограммах, '
    'используйте точку в качестве разделителя - например, 61.5 '))
while user_weight < 1 or user_weight > 300:
    print("Вес не может принимать такие значения!")
    user_weight = float(input(
        'Укажите ваш вес в килограммах, '
        'используйте точку в качестве разделителя - например, 61.5 '))

user_height = float(input(
    'Укажите ваш рост в метрах,'
    ' Используйте точку в качестве разделителя - например, 1.75 '))
while user_height < 0.5 or user_height > 3:
    print("Рост не может принимать такие значения!")
    user_height = float(input(
        'Укажите ваш рост в метрах,'
        ' Используйте точку в качестве разделителя - например, 1.75 '))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Рассчитываем bmi (Индекс массы тела)
def calculate_bmi(user_weight, user_height):
    """Рассчитываем ИМТ."""
    return user_weight / (user_height ** 2)


# Подсчет воды: вес * 30 мл
def calculate_water(user_weight):
    """Рассчитываем необходимое количество воды в день."""
    return user_weight * WATER_PER_KG


# 4. Запись расчетов функций в переменные
# Рассчитываем ИМТ и необходимое количество воды
bmi = calculate_bmi(user_weight, user_height)
water_needed_ml = calculate_water(user_weight)
water_needed_l = water_needed_ml / ML_PER_L


# 5. Определитель, как выводить возраст
# запись значения в зависимости от возраста в переменную
def age_formatting(user_age):
    """Определить, как правильно выводить возраст."""
    if (user_age % 100 == 11
            or user_age % 100 == 12
            or user_age % 100 == 13
            or user_age % 100 == 14):
        return "лет"
    elif user_age % 10 == 1:
        return "год"
    elif (user_age % 10 == 2
            or user_age % 10 == 3
            or user_age % 10 == 4):
        return "года"
    else:
        return "лет"


age_format = age_formatting(user_age)

# 6. Вывод красивого результата
# Выводим приветствие
# Указываем возраст, ИМТ и норму воды.
print()
print('=' * 10)
print(
    f'Привет, {user_name}!\n'
    f'Ваш возраст: {user_age} {age_format}\n'
    f'Ваш ИМТ: {bmi:.1f}\n'
    f'Ваша норма воды: {water_needed_l:.2f} литров в день.\n')
print('Расчет окончен. Будьте здоровы!')

'''спеціальний вбудований модуль datetime надає класи для маніпуляцій з датами і часом:
визначення поточної дати і часу;
обчислення інтервалу між двома подіями;
визначення дня тижня, високосного року для будь-якої дати у минулому не раніше року datetime.MINYEAR або в майбутньому не пізніше року datetime.MAXYEAR;
порівняння дати і часу декількох подій за допомогою операторів порівняння;
робота з часовими зонами, порівняння подій з урахуванням часових зон та переходу на літній/зимовий час;
перетворення дати/часу в рядок і навпаки.'''

import datetime

now = datetime.datetime.now() #отримання поточної дати і часу (рік-місяць-день години:хвилини:секунди.мікросекунди)
print(now) # 2026-03-09 12:15:57.885059

date_part = datetime.date(2026, 3, 9) # Створення об'єктів date і time
time_part = datetime.time(12, 30, 15)
combined_datetime = datetime.datetime.combine(date_part, time_part)# Комбінування дати і часу в один об'єкт datetime
print(combined_datetime)  # Виведе "2026-03-09 12:30:15"

###

specific_date = datetime.datetime(year=2020, month=1, day=7) # Створення об'єкта datetime з конкретною датою
print(specific_date)  # Виведе "2020-01-07 00:00:00"

specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15) # Створення об'єкта datetime з конкретною датою і часом
print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

#-------------



from datetime import datetime #об'єкт datetime в свій скрипт можемо отримати, витягнувши його з модуля

current_datetime = datetime.now()

print(current_datetime.date()) # 2026-03-09
print(current_datetime.time()) # 12:23:40.256534

print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
print(current_datetime.tzinfo) # часова зона об'єкта datetime, якщо часова зона не була вказана- None.


#now = datetime.now() # Створення об'єкта datetime
day_of_week = datetime.now().weekday() # Отримання номера дня тижня
print(f"Сьогодні: {day_of_week}") # Поверне число від 0 (понеділок) до 6 (неділя)


datetime1 = datetime(2023, 3, 14, 12, 0)# Створення двох об'єктів datetime
datetime2 = datetime(2023, 3, 15, 12, 0)
# Порівняння дат
print(datetime1 == datetime2)  # False
print(datetime1 != datetime2)  # True, тому що дати різні
print(datetime1 < datetime2)   # True
print(datetime1 > datetime2)   # False



##---------------------

from datetime import timedelta #використовується для представлення різниці між двома моментами в часі

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta) #64 days, 8:05:56.000010


seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0 виконали конвертацію timedelta в секунди


now = datetime.now()
future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
print(future_date) # 2026-03-19 12:49:37.396553



seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)
print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00



date = datetime(year=2023, month=12, day=18)# Створення об'єкта datetime
ordinal_number = date.toordinal()# Отримання порядкового номера (кількість днів з 1 січня року 1 нашої ери, тобто з початку християнського календаря)
print(f"Порядковий номер дати {date} становить {ordinal_number}") #Порядковий номер дати 2023-12-18 00:00:00 становить 738872 


napoleon_burns_moscow = datetime(year=1812, month=9, day=14)# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
current_date = datetime.now()# Поточна дата
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()# Розрахунок кількості днів
print(days_since) #77973



''' timestamp (часова мітка) є універсальним способом представлення конкретного моменту в часі,
в операційних системах та програмних мовах, адже він не залежить від часових зон і календарних систем.
представляється як кількість секунд з певної початкової дати 
(1 січня 1970 року в UTC, це часовий пояс Гринвіча)'''

now = datetime.now()# Поточний час
timestamp = datetime.timestamp(now)# Конвертація datetime в timestamp
print(timestamp)  # Виведе timestamp поточного часу 1773054483.874405


timestamp = 1617183600# Припустимо, є timestamp
dt_object = datetime.fromtimestamp(timestamp)# Конвертація timestamp назад у datetime
print(dt_object)  # Виведе відповідний datetime 2021-03-31 12:40:00


'''метод strftime використовується для форматування об'єктів дати та часу datetime у рядки 
за допомогою специфічних форматних кодів datetime_object.strftime(format)
%Y - рік з чотирма цифрами (наприклад, 2023).
%y - рік з двома цифрами (наприклад, 23).
%m - місяць як номер (наприклад, 03 для березня).
%d - день місяця як номер (наприклад, 14).
%H - година (24-годинний формат) (наприклад, 15).
%I - година (12-годинний формат) (наприклад, 03).
%M - хвилини (наприклад, 05).
%S - секунди (наприклад, 09).
%A - повна назва дня тижня (наприклад, Tuesday).
%a - скорочена назва дня тижня (наприклад, Tue).
%B - повна назва місяця (наприклад, March).
%b або %h - скорочена назва місяця (наприклад, Mar).
%p - AM або PM для 12-годинного формату.
'''

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")# Форматування дати і часу
print(formatted_date) #2026-03-09 13:19:09

formatted_date_only = now.strftime("%A, %d %B %Y")# Форматування лише дати
print(formatted_date_only) # Monday, 09 March 2026

formatted_time_only = now.strftime("%I:%M %p")# Форматування лише часу
print(formatted_time_only) # 01:19 PM

formatted_date_only = now.strftime("%d.%m.%Y")# Форматування лише дати
print(formatted_date_only) #09.03.2026


'''Метод strptime - перетворення рядків (з текстових файлів, користувацького вводу, 
веб-запитів, баз даних) у об'єкти datetime, якими легко маніпулювати в коді.

datetime_object = datetime.strptime(string, format)
'''

date_string = "2023.03.14"# Припустимо, у нас є дата у вигляді рядка
datetime_object = datetime.strptime(date_string, "%Y.%m.%d")# Перетворення рядка в об'єкт datetime
print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу 2023-03-14 00:00:00




'''ISO формат дати відноситься до міжнародного стандарту представлення дат і часу, 
відомого як ISO 8601. Цей стандарт створений Міжнародною організацією стандартизації (ISO) 
та використовується для уніфікації представлення дати та часу у всьому світі.
"YYYY-MM-DDTHH:MM:SS"
ISO 8601 також підтримує представлення часових зон. Наприклад, "Z" на кінці означає UTC
(Coordinated Universal Time), а відхилення від UTC може бути представлене як 
"+HH:MM" або "-HH:MM". 
UTC є основною системою часу, від якої регулюються всі часові зони у світі.
Він використовується як світовий стандарт часу.
Він не змінюється з порами року та не підлягає переходу на літній/зимовий час.

Метод isoweekday() корисний у сценаріях, де потрібно визначити конкретний день тижня, 
наприклад, при плануванні подій або виконанні дій, залежних від дня тижня. 
Метод isocalendar() корисний у ситуаціях, коли потрібно працювати з тижневими інтервалами або розраховувати дати у форматі, 
який широко використовується в бізнес-плануванні та логістиц'''


iso_format = now.isoformat()# Конвертація у формат ISO 8601 2026-03-09T13:42:53.858891
print(iso_format)

iso_date_string = "2023-03-14T12:39:29.992996"
date_from_iso = datetime.fromisoformat(iso_date_string)# Конвертація з ISO формату
print(date_from_iso) #2023-03-14 12:39:29.992996

now = datetime.now()
day_of_week = now.isoweekday()# Використання isoweekday() для отримання дня тижня
print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня


iso_calendar = now.isocalendar()
print(iso_calendar) # datetime.IsoCalendarDate(year=2026, week=11, weekday=1) це кортеж
print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
# ISO рік: 2026, ISO тиждень: 11, ISO день тижня: 1



##
from datetime import datetime, timezone, timedelta

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)
print(local_now) # 2026-03-09 13:46:56.359808
print(utc_now)  # 2026-03-09 11:46:56.359808+00:00


utc_time = datetime.now(timezone.utc)
# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time) #2026-03-09 06:52:14.266627-05:00

local_timezone = timezone(timedelta(hours=2))# Припустимо, місцевий час належить до часової зони UTC+2(Київ)
local_time = datetime(year=2026, month=3, day=9, hour=13, minute=54, second=0, tzinfo=local_timezone)
utc_time = local_time.astimezone(timezone.utc)# Конвертація локального часу в UTC
print(utc_time)  # Виведе час в UTC 2026-03-09 11:54:00+00:00


timezone_offset = timezone(timedelta(hours=2))  # Наприклад, UTC+2
timezone_datetime = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=timezone_offset)
iso_format_with_timezone = timezone_datetime.isoformat()# Конвертація у формат ISO 8601
print(iso_format_with_timezone) #2023-03-14T12:30:00+02:00


####----------------------------------------

'''Модуль time  надає функції для роботи з часом, зокрема з часовими мітками timestamps, 
паузами виконання для програми, логування, таймінгу операцій, форматування часу для відображення користувачам.'''

import time

current_time = time.time() # поточний час у секундах з 1 січня 1970 року (epoch time).
print(f"Поточний час: {current_time}") #Поточний час: 1773057934.4020667

readable_time = time.ctime(current_time) #перетворює часову мітку (кількість секунд) у зрозуміле
#для людини текстове представлення. Якщо аргумент не вказаний, використовується поточний час.
print(f"Читабельний час: {readable_time}") #Читабельний час: Mon Mar  9 14:06:47 2026

'''Об'єкт time.struct_time в Python є іменованим кортежем, кожен елемент якого має особливе значення,
що представляє певний компонент дати та часу:
tm_year - рік
tm_mon - місяць від 1 до 12
tm_mday - день місяця від 1 до 31
tm_hour - години від 0 до 23
tm_min - хвилини від 0 до 59
tm_sec - секунди від 0 до 59
tm_wday - день тижня від 0 до 6
tm_yday - день року від 1 до 366
tm_isdst - прапорець літнього часу. 0 означає, що літній час не діє, 
           -1 - інформація відсутня, 1 - літній час діє'''

local_time = time.localtime(current_time) #перетворює часову мітку в структуру struct_time у місцевій часовій зоні
print(f"Місцевий час: {local_time}") # Місцевий час: time.struct_time(tm_year=2026, tm_mon=3, tm_mday=9, tm_hour=16, tm_min=54, tm_sec=39, tm_wday=0, tm_yday=68, tm_isdst=0)

local_time = time.gmtime(current_time) #перетворює часову мітку в структуру struct_time у у UTC
print(f"Місцевий час: {local_time}") #Місцевий час: time.struct_time(tm_year=2026, tm_mon=3, tm_mday=9, tm_hour=14, tm_min=54, tm_sec=39, tm_wday=0, tm_yday=68, tm_isdst=0)


'''метод time.perf_counter(), який надає доступ до лічильника з високою точністю, 
є ідеальним для вимірювання коротких інтервалів часу.
використовується в основному для визначення часу виконання коду.
'''
start_time = time.perf_counter()# Записуємо час на початку виконання
for _ in range(1_000_000):# Виконуємо якусь операцію
    pass  # Просто проходить цикл мільйон разів
end_time = time.perf_counter()# Записуємо час після виконання операції
execution_time = end_time - start_time# Розраховуємо та виводимо час виконання
print(f"Час виконання: {execution_time} секунд") #Час виконання: 0.15181049999955576 секунд

'''в Python представлення чисел з підкресленнями _ є способом зробити великі числа більш читабельними. 
Наприклад, число 1_000_000 еквівалентне 1000000.'''

c = 1_000_000_000 # Один мільярд
print(c)  # Виведе 1000000000

'''оператор pass використовується як заповнювач.  Він не робить нічого і використовується там, 
де синтаксис вимагає наявності хоча б однієї інструкції, але вам не потрібно виконувати жодних дій.
pass використовується всередині циклу for - цикл просто проходить мільйон ітерацій, не виконуючи жодної дії на кожній з них.
є корисним для тимчасового "заповнення" місця в коді, що дозволяє вашій програмі виконуватися, 
навіть коли певні частини ще не були реалізовані.
'''

def my_function():
    pass

print("Початок паузи")
time.sleep(5) #зупиняє виконання програми на вказану кількість секунд
print("Кінець паузи")




'''два основних типи випадкових величин: 
Дискретні - такі, які приймають обмежену кількість значень або значення, які можна перелічити.
Неперервні - можуть приймати будь-яке значення у певному діапазоні.
Для генерації випадкових (псевдовипадкових) чисел у Python є пакет random.
Для отримання випадкового цілого числа з рівномірного розподілу в інтервалі між a та b включно -
метод random.randint(a, b), який повертає випадкове ціле число N таке, що a <= N <= b:
'''

import random

dice_roll = random.randint(1, 6) #симуляція кидка кубика
print(f"Ви кинули {dice_roll}") #Ви кинули 5

'''Метод random.random() потрібен, щоб отримати випадкове число в інтервалі 0, 1.
Він генерує випадкове дійсне число між 0.0 (включно) та 1.0 (не включно)'''

num = random.random()
print(num) #0.976954229274743

'''Вираз .2 це кількість знаків після десяткової крапки. 
У цьому випадку вказано, що потрібно відображати два знаки для дійсного числа. 
Символ f означає, що число має бути відображене у форматі дійсного числа.'''

fill_percentage = random.random() * 100
print(f"Заповнення: {fill_percentage:.2f}%") #Заповнення: 11.64%

'''Метод random.randrange(start, stop[, step]) повертає випадково вибране число з заданого діапазону.'''

print(random.randrange(10))  # Верхня межа є 10, але не включається

target = random.randrange(1, 11, 2) #симуляція пострілу по мішені, але необхідно вибрати 
                                    # випадковий номер від 1 до 10, та лише непарні числа:
print(f"Ціль: {target}") #Ціль: 9



'''Коли є список об'єктів і потрібно перемішати порядок елементів в цьому списку на випадковий,
 ми використовуємо метод random.shuffle(x), де x - список, який потрібно перемішати.'''

cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Перемішана колода: {cards}") #Перемішана колода: ['Дама', '7', '8', 'Король', '10', 'Туз', 'Валет', '6', '9']



'''Якщо потрібно вибрати випадковий елемент зі списку, нам потрібно використати 
метод random.choice(seq), де seq - послідовність для вибору: список або кортеж.'''

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits)) # banana

'''метод random.choices() використовується для генерації випадкової вибірки із послідовності.
 може повернути один або декілька елементів з вказаної послідовності, 
 при цьому дозволяючи повторення елементів у вибірці.
 random.choices(population, weights=None, cum_weights=None, k=1)
population - послідовний список, з якого має бути зроблений вибір.
weights - опціональний список, який вказує ймовірності (ваги) кожного елемента в списку population.
Ці ваги визначають, наскільки ймовірно, що конкретний елемент буде обраний.
Довжина списку weights має дорівнювати довжині списку population.
cum_weights - теж опціональний список кумулятивних ваг. Якщо він вказаний, то список weights ігнорується.
Кумулятивна вага кожного елемента визначається як сума його ваги плюс ваги всіх попередніх елементів.
k: Кількість елементів для вибору. За замовчуванням k=1.
 '''
items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item) #['банан']

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers) #[5, 3, 2]

colors = ['червоний', 'зелений', 'синій']
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color) #['червоний']

participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
team = random.sample(participants, 4)
print(f"Команда: {team}") #Команда: ['Богдан', 'Зорян', 'Віктор', 'Женя']



'''random.uniform(a, b). Метод повертає випадкове дійсне число N, таке що a <= N <= b'''

price = random.uniform(50, 100)
print(f"Випадкова ціна: {price:.2f}") #Випадкова ціна: 88.27




#############################################################################
'''Пакет math у Python надає доступ до математичних функцій, 
визначених стандартом мови C. Цей пакет включає функції для різних математичних операцій,
включаючи тригонометричні обчислення, логарифми, квадратний корінь та інше.
Константи, які надає цей пакет:
math.pi - константа π (приблизно 3.14159...);
math.e - константа e, основа натуральних логарифмів (приблизно 2.71828...);
math.tau - константа τ, дорівнює 2π (приблизно 6.28318...);
math.inf - позначення нескінченності;
math.nan - позначення 'Not a Number' (не число);'''

import math

x = 3.7

ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)

'''Тригонометричні функції
math.sin(x) - синус x, де x в радіанах;
math.cos(x) - косинус x;
math.tan(x) - тангенс x;
math.asin(x) - арксинус x;
math.acos(x) - арккосинус x;
math.atan(x) - арктангенс x;

Експоненційні та логарифмічні функції
math.exp(x) - число e в ступені x;
math.log(x[, base]) - Логарифм x за основою base. Якщо base не вказано, обчислюється натуральний логарифм;

math.pow(x, y) - x у ступені y;
math.sqrt(x) - квадратний корінь з x;

math.fabs(x) - модуль (абсолютне значення) x;
math.factorial(x) - факторіал числа x;
math.gcd(x, y) - найбільший спільний дільник для x та y;'''

print(math.pi)  # Виведе приблизне значення π  3.141592653589793




angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута   0.8660254037844386

print(math.sqrt(9))  # Квадратний корінь з 9   3.0

print(math.log(10, 2))  # Логарифм 10 за основою 2  3.3219280948873626

'''пакет cmath  надає той самий API, але вміє працювати з комплексними числами.'''



####

'''Дійсні числа в комп'ютерних програмах часто можуть викликати неточності через їхню бінарну природу.'''

print(0.1 + 0.2 == 0.3)  # False

print(0.1 + 0.2) # 0.30000000000000004


r = math.isclose(0.1 + 0.2, 0.3) # використовується для порівняння двох чисел з певною допустимою похибкою
print(r)  # True

r = math.isclose(0.1, 0.10000000009)
print(r)  # True


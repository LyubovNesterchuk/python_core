'''У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. 
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, 
яка допоможе вам визначати, кого з колег потрібно привітати. 
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача 
та його день народження. 
Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це 
та переносити дату привітання на наступний робочий день, якщо це необхідно.'''


from datetime import datetime, date, timedelta

users = [
    {"name": "Bill Gates", "birthday": "1995.3.15"},
    {"name": "Steve Jobs", "birthday": "2000.3.21"},
    {"name": "Jinny Lee", "birthday": "1996.3.12"},
    {"name": "Sarah Lee", "birthday": "1987.3.13"},
    {"name": "Jonny Lee", "birthday": "1978.3.22"},
    {"name": "John Doe", "birthday": "1982.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# приймає рядкове представлення дати в форматі "YYYY.MM.DD" і перетворює його на об'єкт datetime.date
def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

# приймає об'єкт datetime.date і повертає рядкове представлення дати в форматі "YYYY.MM.DD"
def date_to_string(date):
    return date.strftime("%Y.%m.%d")

'''date_string = "2026.03.11"
converted_date = string_to_date(date_string)
print(converted_date) # 2026-03-11
date_string = date_to_string(converted_date)
print(date_string) # 2026.03.11'''

# приймає список імен користувачів та їх дат народження у рядковому форматі, і повертає 
# список словників у форматі {"name": <name>, "birthday": <birthday>}, 
# де <birthday> - це об'єкт datetime.date
def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

prepared_users = prepare_user_list(users)
'''print(prepared_users)
[{'name': 'Bill Gates', 'birthday': datetime.date(1995, 3, 15)}, 
 {'name': 'Steve Jobs', 'birthday': datetime.date(2000, 3, 21)}, 
 {'name': 'Jinny Lee', 'birthday': datetime.date(1996, 3, 12)}, 
 {'name': 'Sarah Lee', 'birthday': datetime.date(1987, 3, 13)}, 
 {'name': 'Jonny Lee', 'birthday': datetime.date(1978, 3, 22)},
 {'name': 'John Doe', 'birthday': datetime.date(1982, 1, 23)}, 
 {'name': 'Jane Smith', 'birthday': datetime.date(1990, 1, 27)}] '''

# який день тижня відповідає start_date
def find_next_weekday(start_date, weekday):
    # скільки днів залишилося до наступного бажаного дня тижня weekday
    days_ahead = weekday - start_date.weekday() 
    # Якщо результат виходить меншим або дорівнює 0, це означає, що шуканий день тижня уже минув 
    # у цьому тижні, і тому до різниці додається 7, щоб перейти до наступного тижня.
    if days_ahead <= 0: 
        days_ahead += 7
    # функція додає обчислену кількість днів days_ahead до start_date, використовуючи timedelta(). Це дає 
    # нову дату, яка є наступним weekday після start_date
    return start_date + timedelta(days=days_ahead)

# перенесення дати на наступний робочий день (понеділок-0), якщо день народження припадає на вихідний.
# adjust_for_weekend → «коригувати_з_урахуванням_вихідних»
def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday

# Перевірте, чи належить день народження до періоду від сьогоднішнього дня до days днів вперед.
def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today() # Повертає тільки дату (рік, місяць, день)
#today = datetime.now().date() # datetime.now() - дата і точний час (2026-03-11 14:25:18.374920)

# визначити дату дня народження в поточному році
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)

# якщо день народження вже був цього року → беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

# Якщо різниця лежить в діапазоні від 0 до days, то день народження має бути включений 
# до фінального списку.
        if 0 <= (birthday_this_year - today).days <= days:
            birthday_this_year = adjust_for_weekend(birthday_this_year)

# відформатувати дату дня народження в формат рядка 
            congratulation_date_str = date_to_string(birthday_this_year)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })

    return upcoming_birthdays



print(get_upcoming_birthdays(prepared_users, days=7))

'''[{'name': 'Bill Gates', 'congratulation_date': '2026.03.16'}, 
{'name': 'Jinny Lee', 'congratulation_date': '2026.03.12'}, 
{'name': 'Sarah Lee', 'congratulation_date': '2026.03.13'}]'''
'''Правильний спосіб отримати модифікований контейнер — це використовувати пакет collections 
та класи UserList, UserDict, UserString, які в ньому є.
Всі ці класи поводяться точно як вбудовані контейнери з тією лише відмінністю, що самі дані 
лежать у полі data у цих класів і ви можете використовувати це поле на свій розсуд.'''


'''UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника. 
Він дозволяє легше створювати власні класи словників, модифікуючи або додаючи нову поведінку 
до стандартних методів словника.
'''

from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}


#------------------------------------------


contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]

# створимо клас Customer, який наслідує від UserDict з модуля collections та розширює можливості 
# UserDict двома методами
class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"
    
# Щоб скористатися можливостями створеного класу нам необхідно створити новий список customers, 
# в якому кожен елемент списку contacts перетворюється на екземпляр класу Customer. 
# Це дозволить нам використовувати визначені в класі методи для кожного контакту.
if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

# виконуємо ітерації по списку customers: перший раз для виведення інформації про телефони 
# контактів через виклик методу phone_info, а другий раз - для виведення інформації про 
# електронні адреси через виклик методу email_info
    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())

    print("---------------------------")

'''---------------------------
Allen Raymond: (992) 914-3792
Chaim Lewis: (294) 840-6685
Kennedy Lane: (542) 451-7038
---------------------------
Allen Raymond: nulla.ante@vestibul.co.uk
Chaim Lewis: dui.in@egetlacus.ca
Kennedy Lane: mattis.Cras@nonenimMauris.net
---------------------------'''

#-------------------------------------------

class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys


'''UserList - це клас, який дозволяє створювати власні версії списків з додатковими функціями. 
Ви можете додавати нові методи або змінювати ті, що вже існують, щоб вони працювали по-іншому.'''

from collections import UserList

class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, 
    # якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)

# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list) # Оригінальний список: [1, 2, 3]

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list) # Оновлений список: [1, 2, 3, 4]

# клас MyList наслідує від UserList і додає метод add_if_not_exists, який дозволяє додати елемент
# до списку, лише якщо він ще не існує у списку. При цьому в іншому my_list веде себе як 
# звичайний список.


#----------------------------------

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum()) # 15

# створили клас, який поводиться як список, але в ньому є метод sum , який повертає суму всього 
# вмісту цього класу, при цьому перетворюючи рядки на цілі числа.


#------------------------------

payment = [1, -3, 4]

class AmountPaymentList(UserList):
    def __init__(self, payment):
        self.payment = payment
    def amount_payment(self):
        sum = 0
        for value in self.payment:
            if value > 0:
                sum = sum + value
        return sum



'''UserString дозволяє створювати класи, які наслідують поведінку звичайного рядка, 
з можливістю додавання нових методів або зміни стандартної поведінки рядків.'''


from collections import UserString

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string) # Рядок: radar
print("Чи є паліндромом?", my_string.is_palindrome()) # Чи є паліндромом? True

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string) # Рядок: hello
print("Чи є паліндромом?", another_string.is_palindrome()) # Чи є паліндромом? False


#-------------------------------------------------------

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts) # hello w

#---------------------------------------

class NumberString(UserString):
    def __init__(self, value):
        super().__init__(value)

    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count
    


'''Модуль dataclasses в Python надає засіб для декларативного визначення класів, які переважно 
використовуються для зберігання даних. Цей модуль введений у Python 3.7, щоб спростити створення 
таких класів без необхідності ручного написання бойлерплейт (від англ. - boilerplate) коду, 
який часто повторюється у традиційних класах.
Модуль надає декоратор класу @dataclass який спрощує створення класів для зберігання даних. 
Традиційно, коли ми створюємо клас для зберігання даних, нам потрібно вручну визначити метод 
як-от __init__() для ініціалізації атрибутів, магічні методи для представлення об'єкта 
у зрозумілому форматі або для порівняння об'єктів. 
Використання @dataclass дозволяє зменшити кількість коду, необхідного для створення класів, 
які в основному зберігають дані. Це робить код більш читабельним і легшим для розуміння, 
а також автоматично створює конструктор класу __init__.'''

'''декоратор @dataclass використовується, коли ви створюєте класи, що слугують для 
зберігання даних і не потребують складної логіки обробки. Наприклад, класи, 
що представляють сутності в базі даних, конфігураційні об'єкти, об'єкти передачі даних між 
компонентами системи тощо.'''

'''Традиційно, якщо вам потрібно створити клас для зберігання даних, ви б мали б вручну 
визначити метод __init__ для ініціалізації атрибутів.'''

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

'''Якщо використати декоратор @dataclass, ми можемо автоматизувати створення класу, значно 
спростивши код.'''

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

@dataclass
class Article:
    title: str
    author: str
    views: int = 0


#----------------------------------------------
# створимо клас Rectangle, який буде обчислювати та виводити площу різних прямокутників, 
# заданих користувачем

# ми визначаємо клас Rectangle за допомогою @dataclass, Python автоматично створює 
# метод __init__, який приймає атрибути width та height як параметри, за нас. 
# Це означає, що нам не потрібно явно визначати конструктор класу.
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height
    
# екземпляри класу Rectangle
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

# Кожен екземпляр класу Rectangle має метод area, який обчислює та повертає площу прямокутника, 
# використовуючи атрибути width та height
print(f"Площа прямокутника 1: {rect1.area()}") # Площа прямокутника 1: 50
print(f"Площа прямокутника 2: {rect2.area()}") # Площа прямокутника 2: 21
print(f"Площа прямокутника 3: {rect3.area()}") # Площа прямокутника 2: 21



'''Перелічуваний тип даних (Enumeration), часто скорочено як Enum, - це спосіб визначення набору 
іменованих констант у мовах програмування, що дозволяє використовувати більш зрозумілі імена для 
цих констант замість простих числових значень.
Перелічення зустрічаються в ситуаціях, де потрібно представити обмежену кількість варіантів:
Дні тижня
Статуси замовлень (наприклад, "новий", "в обробці", "відправлений", "доставлений")
Ролі чи рівні доступу в системі безпеки ('користувач', 'модератор', 'адміністратор')'''

'''Модуль enum в Python надає можливість для створення перелічуваних типів, які дозволяють 
визначати іменовані константи. Ці константи можуть бути використані для покращення читабельності 
та надійності коду, замінюючи використання неявних значень, таких як рядки або числа, 
на більш зрозумілі імена.
Клас Enum з модуля enum дозволяє об'єднати ряд іменованих констант і гарантувати, 
що об'єкти цього класу можуть приймати тільки одне з обмежених значень, які вони описують.

Для створення перелічення використовується наслідування від класу Enum. 
Кожен атрибут класу представляє окремий член перелічення.

Зміна або додавання нових значень в Enum не впливає на решту коду, що робить зміну (рефакторінг) 
та розширення коду простішими. '''

from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today = Day.MONDAY
print(today)  # Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.") # Сьогодні понеділок.

print(today.name)  # MONDAY
print(today.value)  # 1

day_from_value = Day(1)
print(day_from_value)  # Day.MONDAY

#--------------------------------------------------------------

from enum import Enum, auto

# використали функцію auto(), щоб автоматично присвоїти унікальні значення кожному статусу, 
# уникаючи необхідності вручну вказувати їх.

class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELED = auto()

# створимо клас Order, який буде використовувати наш перелічуваний тип даних OrderStatus 
# для відстеження статусу замовлення   
 
class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")

order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status() # Статус замовлення 'Ноутбук': NEW.
order2.display_status() # Статус замовлення 'Книга': NEW.

order1.update_status(OrderStatus.PROCESSING) # Замовлення 'Ноутбук' оновлено до статусу PROCESSING.
order2.update_status(OrderStatus.SHIPPED) # Замовлення 'Книга' оновлено до статусу SHIPPED.

order1.display_status() # Статус замовлення 'Ноутбук': PROCESSING.
order2.display_status() # Статус замовлення 'Книга': SHIPPED.



'''Наслідування створює тісну залежність між базовим класом та похідними класами. 
Зміни в базовому класі можуть несподівано вплинути на поведінку похідних класів. 
Наслідування може призвести до спадкування методів, які не мають сенсу для похідного класу, 
що може призвести до неочікуваної або помилкової поведінки.'''

class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat(Owner):
    def __init__(self, nickname, age, name, phone):
        super().__init__(name, phone)
        self.nickname = nickname
        self.age = age

    def cat_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"
    
    def sound(self):
		        return "Meow"

cat = Cat('Simon', 4, 'Boris', '+380503002010')
print(cat.info()) # Boris: +380503002010
print(cat.cat_info()) # Cat Name: Simon, Age: 4
# Це б виглядало так, ніби ми кажемо: "Кішка є господарем".



'''Асоціація в ООП - це концепція, яка описує відносини між класами через їх об'єкти. 
клас може включати в себе інший клас як одне зі своїх полів, що описується словом "має".
Асоціація поділяється на два основних типи: композиція та агрегація'''

'''Агрегація - це тип відношення між об'єктами, яке також представляє відносини "ціле" 
до "частини", але в цьому випадку "частини" можуть існувати незалежно від "цілого". 
Це означає, що якщо "ціле" буде знищено, "частини" можуть продовжувати існувати самостійно. 
Агрегація вказує на більш слабку залежність між об'єктами і часто використовується, 
коли об'єкти можуть входити до складу різних груп або колекцій. '''

# Натомість, ми повинні показати, що кішка "має" господаря. Це не робить кішку господарем. 
# Просто означає, що між кішкою та людиною є зв'язок. Людина - це господар кішки, 
# а кішка - це вихованець цієї людини.
class Owner:
   def __init__(self, name: str, phone: str):
       self.name = name
       self.phone = phone

   def info(self):
       return f"{self.name}: {self.phone}"

class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
       self.nickname = nickname
       self.age = age
       self.owner = owner

    def get_info(self):
       return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
       return "Meow"

owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)

print(cat.owner.info()) # Boris: +380503002010
print(cat.get_info()) # Cat Name: Simon, Age: 4
# "Кішка має господаря"


'''Композиція - це тип відношення між об'єктами, де один об'єкт є частиною іншого. 
У відношенні композиції "частина" не може існувати без "цілого". Це означає, 
що якщо "ціле" буде знищено або видалено, то "частина" також буде знищена або видалена.'''

# кожен "Проект" (клас Project), може містити кілька "Задач" (клас Task), і ці задачі 
# не мають сенсу поза контекстом свого проекту. Якщо проект видаляється, то всі його задачі 
# також повинні бути видалені.

class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = [] 

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info() 
'''Проект: Веб-розробка
Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки.
Задача: Розробка API, Опис: Реалізувати ендпоінти для користувачів.'''

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()
'''Проект: Веб-розробка
Задача: Дизайн інтерфейсу, Опис: Створити макет головної сторінки.'''
# Композиція дозволяє інкапсулювати поведінку та дані, пов'язані з управлінням задачами, 
# всередині класу Project, що робить систему більш організованою та зрозумілою.




'''обробка винятків у Python здійснюється за допомогою конструкції try/except. 
Це дозволяє програмі продовжувати виконання, навіть якщо виникає помилка.
Ви можете специфікувати різні типи винятків, які хочете обробити, або використовувати 
загальний виняток, щоб перехопити будь-яку помилку.'''

try:
    # Код, який може викликати виняток
    result = 10 / 0
    # result = 10 / vjk
except ZeroDivisionError:
    # Обробка винятку ділення на нуль
    print("Ділення на нуль!") # Ділення на нуль!
except Exception as e:
    # Обробка будь-якого іншого винятку
    print(f"Виникла помилка: {e}") # Виникла помилка: name 'vjk' is not defined
else:
    # Виконується, якщо виняток не був викликаний
    print("Все пройшло успішно!")
finally:
    # Виконується завжди, незалежно від того, був виняток чи ні
    print("Блок finally завжди виконується.")  # Блок finally завжди виконується.


'''Коли ж ви пишете свій застосунок вам може знадобитися створити свої власні винятки, 
щоб обробляти їх на рівні вище. Створення власних винятків у Python дозволяє краще керувати 
помилками у вашому коді, роблячи його більш гнучким та зрозумілим для інших розробників. 
Для цього вам потрібно визначити клас винятку, який наслідується від класу Exception 
або одного з його підкласів.'''


# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"): # значення за замовчуванням для повідомлення
        self.message = message
        super().__init__(self.message)

# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи меньший за 18 років")
        #raise AgeVerificationError() # Виняток: Вік не задовольняє мінімальній вимозі
if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}") # Виняток: Вік особи меньший за 18 років
    else:
        print("Вік перевірено, особа доросла.")


#---------------------------------------------------------------------------------
class NameTooShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name

if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
'''
Enter name: Bob
Hello, Bob

Enter name: bob
Name should start from capital letter

Enter name: Bo
Name is too short, need more than 2 symbols
'''
#---------------------------------------------------------------------------




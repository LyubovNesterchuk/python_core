'''У програмуванні поняття "функція як об'єкт першого класу" означає, що функції 
в мові програмування використовуються як звичайні об'єкти. Це означає, що функції 
можна присвоювати змінним, передавати як аргументи іншим функціям, 
повертати як результати інших функцій, а також зберігати в структурах даних, 
таких як списки, словники або класи.'''

#--------------------------------------
# присвоїмо функцію змінній

def my_function():
    print("Hello, world!")
f = my_function
f() # Hello, world!


#--------------------------------------
# Функції можуть бути аргументами інших функцій. 

'''створити функцію, яка приймає іншу функцію, як аргумент та використовує її для обчислення результату.'''

from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

# параметр operation це функція, яка приймає два цілі числа та повертає ціле число
def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply) # 8 15


#---------------------------------------------------------------------
# Функції можуть повертають інші функції.

'''створити функцію, яка генерує іншу функцію для підняття числа до заданого степеня.'''

def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner
# Використання
square = power(2)
cube = power(3)

print(square(4)) # 16
print(cube(4)) # 64


#------------------------------------------------------------
# зберігання функцій у структурах даних. 

'''створимо словник, де ключами будуть назви операцій, а значеннями — відповідні функції'''

from typing import Dict

# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25

print(result_add)  # 30
print(result_square)  # 25



#-----------------------------------------------

'''Замикання (closure) відбувається, коли внутрішня функція запам'ятовує стан свого оточення 
в момент свого створення і може використовувати ці змінні навіть після того, як зовнішня функція 
завершила своє виконання.

Ключові аспекти замикань:

Внутрішня функція має доступ до змінних, визначених у області видимості зовнішньої функції.
Зовнішня функція повертає внутрішню функцію як результат своєї роботи.
Після завершення роботи зовнішньої функції, внутрішня функція зберігає доступ до цих змінних'''

# Замість того щоб безпосередньо викликати inner_function, outer_function після свого виконання 
# повертає її як об'єкт. Це дозволяє функції inner_function зберегти зв'язок 
# зі своїм лексичним середовищем, навіть після завершення виконання outer_function.
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function
# Створення замикання
my_func = outer_function("Hello, world!")
my_func() # Hello, world!
# Коли виконується дія my_func = outer_function("Hello, world!"), 
# то функція my_func стає посиланням на функцію inner_function. Чому? 
# Тому, що коли викликається функція outer_function, вона повертає посилання на 
# функцію inner_function. Далі коли ми викликаємо my_func() виконується насправді 
# саме функція inner_function , вона успішно виводить "Hello, world!". Це відбувається завдяки 
# збереженню inner_function доступу до змінної message, що була визначена в outer_function. 
# Така поведінка є класичним прикладом замикання, де внутрішня функція зберігає стан змінних 
# зі свого лексичного контексту.


def counter() -> Callable[[], int]:
    count = 0
    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count
    return increment
# Створення лічильника
count_calls = counter()
# Виклики лічильника
print(count_calls())  # 1
print(count_calls())  # 2
print(count_calls())  # 3
# Це приклад замикання, де increment замкнула в собі змінну count і має до неї доступ 
# навіть після того, як зовнішня функція counter завершує своє виконання. 
# Завдяки цьому, count_calls зберігає стан між викликами. 


#-----------------------------------------------

'''Каррінг (currying) — це техніка в програмуванні, коли функція, яка приймає кілька аргументів, 
перетворюється на послідовність функцій, кожна з яких приймає один аргумент.'''

def add(a, b):
    return a + b
#Застосувавши каррінг до цієї функції, ми перетворимо її на двій функції, 
# кожна з яких приймає по одному аргументу
def add(a):
    def add_b(b):
        return a + b
    return add_b
# Використання:
add_5 = add(5)
result = add_5(10)
print(result)
# Тут функція add приймає перший аргумент a і повертає функцію add_b. 
# Сама функція add_b приймає другий аргумент b і повертає результат a + b. 
# Фактично ми перетворили виклик функції add на виклик двох функцій.


'''у нас є функція для обчислення знижки на товар. Ця функція приймає відсоток знижки 
і остаточну ціну товару.'''

def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)
# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price) # 450.0
discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price) # 400.0


# Використовуючи каррінг, ми можемо створити більш гнучку структуру для роботи з різними 
# типами знижок.  кожна з яких буде приймати тільки ціну товару.
def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)
# Застосування знижок
discounted_price = ten_percent_discount(500)  
print(discounted_price) # 450.0
discounted_price = twenty_percent_discount(500) 
print(discounted_price) # 400.0



def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount
# створити словник, де ключами будуть назви знижок, 
# а значеннями — відповідні функції обчислення знижки, створені за допомогою каррінгу
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}
# Використання функції зі словника
price = 500
discount_type = "20%"
discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}") # Ціна зі знижкою 20%: 400.0
# Цей підхід забезпечує велику гнучкість, бо ми можемо легко додавати, видаляти або змінювати 
# знижки в словнику без необхідності зміни основного коду програми.



#-------------------------------------------------------------------------------------------

'''Декоратори в Python — інструмент, який дозволяє змінювати поведінку функцій або методів 
без зміни їхнього вихідного коду. Вони є прикладом функцій вищого порядку, які приймають 
іншу функцію як аргумент та повертають нову функцію.'''

def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner
complicated = logger(complicated) # Декоратор logger приймає функцію як аргумент і повертає нову функцію
print(complicated(2, 3)) # Викликається функція: complicated: 2, 3
                         # Функція complicated завершила виконання: 5
                         # 5
# Декорована функція зберігає свою оригінальну функціональність, але додатково отримує 
# нову поведінку або модифікації.Тепер, викликаючи complicated, ми побачимо у консолі, 
# з якими аргументами її викликали і що вона повернула. 
# При цьому, код самої complicated жодним чином не змінився і спосіб роботи з нею також.


'''Декоратори використовуються з синтаксисом @'''
# Точно той самий код, який робить в точності те саме, можна записати у вигляді
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result
    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y
print(complicated(2, 3))
# Функція logger є декоратором. Вона приймає функцію func і повертає нову функцію inner. 
# Функція inner виконує додаткові дії (логування) до і після виконання func. 
# При оголошенні функції complicated, ми використовуємо @logger, щоб застосувати декоратор. 
# Тепер при кожному виклику complicated будуть виконуватися додаткові дії логування. 
# Тепер у коді явно видно, що complicated була задекорована logger у тому самому місці, 
# де complicated була оголошена.

'''Декоратори широко використовуються для різних цілей. Основні застосування це:
Логування - запис інформації про виклики функцій для забезпечення прозорості та відстеження.
Перевірка доступу - перевірка прав користувача перед виконанням функції, щоб контролювати доступ.
Кешування - збереження результатів функції для підвищення ефективності та скорочення часу виконання.
Перевірка аргументів - аналіз та модифікація аргументів перед їх передачею функції 
для забезпечення правильності виклику.'''

'''модуль functools для збереження метаданих оригінальної функції, яку ми декоруємо.'''

from functools import wraps

def logger(func):
    @wraps(func) # зберігаює інформацію про оригінальну функцію, як-от ім'я функції та документацію
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__) # complicated
# functools.wraps(func) застосовується до внутрішньої функції inner. 
# Вона "копіює" метадані (ім'я функції, документацію тощо) від func до inner. 
# Завдяки цьому, коли ми викликаємо print(complicated.__name__), ми отримуємо метадані 
# оригінальної функції complicated, а не функції inner з декоратору logger.


'''Comprehensions в Python - це спосіб компактного створення колекцій на основі наявних колекцій. 
Python підтримує кілька видів comprehensions: для списків (list comprehensions), 
множин (set comprehensions) та словників (dictionary comprehensions). Вони дозволяють писати 
вирази для створення нових колекцій з меншою кількістю коду, ніж при використанні циклів.'''

'''list comprehensions [new_item for item in iterable if condition]'''
sq = []
for i in range(1, 6):
    sq.append(i**2)
print(sq)  # [1, 4, 9, 16, 25]

sq = [x**2 for x in range(1, 6)]
print(sq) # [1, 4, 9, 16, 25]

#------------
even_squares = []
for x in range(1, 10):
    if x % 2 == 0:
        even_squares.append(x**2)
print(even_squares)  # [4, 16, 36, 64]

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares) # [4, 16, 36, 64]


'''set comprehensions {new_item for item in iterable if condition}'''
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq) # {1, 4, 36, 9, 16, 25}

odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares) # {1, 9, 81, 49, 25}


'''dictionary comprehensions {key: value for item in iterable if condition}'''
sq = {x: x**2 for x in range(1, 10)}
print(sq) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict) # {6: 36, 7: 49, 8: 64, 9: 81}


#------------------------------------------------------------------------------------
'''
лямбда-функції (анонімні функції) використовуються для створення маленьких, однорядкових функцій

lambda arguments: expression

lambda — це ключове слово, що вказує на початок лямбда-функції. 
arguments — це список аргументів, які приймає функція, 
expression — це вираз, який буде виконано та його результат повернуто.'''

print((lambda x, y: x + y)(5, 3))  # 8

nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted) # [5, 4, 3, 2, 1]



'''Один з прикладів використання лямбда-функцій — це генератор map.
Функція map() є функцією вищого порядку, що означає, що вона приймає іншу функцію як аргумент
використовується для застосування заданої функції до кожного елемента об'єкта ітерації.

map(function, iterable, ...)

function - функція, яку треба застосувати до кожного елемента в iterable.
iterable - об'єкт ітерації (список, кортеж тощо), елементи якого будуть оброблятися function
'''

numbers = [1, 2, 3, 4, 5]
# ми отримаємо генератор, яким пройшлися в циклі for та вивели значення на кожній ітерації 
# функцією print.
for i in map(lambda x: x ** 2, numbers):
    print(i) # 1 4 9 16 25 

# Якщо ми хочем отримати список, а не генератор то код можна записати так:
squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)  #  [1, 4, 9, 16, 25]

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)
print(list(sum_nums)) # [5, 7, 9]


'''list comprehensions замість використання функції map():'''
squared_nums = [x * x for x in nums]
print(squared_nums) # [1, 4, 9, 16, 25]

sum_nums = [x + y for x, y in zip(nums1, nums2)]
print(sum_nums) # [5, 7, 9]


'''Функція filter() використовується для фільтрації об'єктів ітерації, таких як списки або кортежі,
за допомогою заданої функції. Вона створює ітератор, який містить тільки ті елементи 
об'єкта ітерації, для яких функція-фільтр повертає True.

у Python можна будь-який тип привести до boolean. 
До False приводяться 0, None та порожні контейнери. 
Рядки, списки, словники, множини, кортежі, всі інші випадки приводяться до True.

filter(function, iterable)

function - функція, яка визначає, чи слід включати елемент у результат. 
Ця функція повинна приймати один аргумент і повертати булеве значення True або False.
iterable - об'єкт ітерації (наприклад, список, кортеж), елементи якого будуть перевірятися 
функцією function
'''

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))
print(list(even_nums)) # [2, 4, 6, 8, 10]


def is_positive(x):
    return x > 0
nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)
print(list(positive_nums)) # [1, 2]


some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'
new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str)


'''можна замінити filter() на list comprehensions:'''
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print(even_nums) # [2, 4, 6]

new_str = ''.join([x for x in some_str if x.islower()])
print(new_str) # идавництво


'''Функція any() є вбудованою функцією, яка повертає True, якщо хоча б один елемент із заданого 
об'єкта ітерації є істинним. Якщо об'єкт ітерації порожній або всі його елементи є хибними, 
то any() повертає False.'''

nums = [0, False, 5, 0]
result = any(nums)  
print(result) # True

'''В функцію можна передавати генератор або list comprehensions. '''
nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result) # False



'''Функція all() є вбудованою функцією, яка повертає True, якщо всі елементи в переданому 
їй об'єкті ітерації є істинними - тобто не False, 0, "", None або будь-яке інше значення, 
яке Python оцінює як хибне. 

якщо об'єкт ітерації порожній, функція all() повертає True.'''

nums = [1, 2, 3, 4]
result = all(nums)  
print(result) # True

is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even) # False

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case) # True





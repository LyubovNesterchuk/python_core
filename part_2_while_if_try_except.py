x = int(input('Введіть число: '))

if x % 2 == 0:
    print("Число x є парним.")
else:
    print("Число x є непарним.")


a = input('Введіть число')
a = int(a)
if a > 0:
    print('Число додатне')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число - нуль')


money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")


result = None
if result:
    print(result)
else:
    print("Result is None, do something")


user_name = input("Enter your name: ")
if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")


# Оператор is у Python використовується для перевірки того, 
# чи два об'єкти вказують на одну і ту ж область пам'яті,
# тобто чи вони є одним і тим же об'єктом.

# оператор == перевіряє рівність значень об'єктів.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True
print(a is c)  # False

# if my_var is None:    # Робимо щось, якщо 'my_var' є 'None'

# для побудови логічних умов з декількох використовується булева алгебра
# оператори not, and, or

name = "Taras"
age = 22
has_driver_licence = True

if name and age >= 18 and has_driver_licence:
    print(f"User {name} can rent a car")



num = int(input("Введіть число: "))
length = len(str(num))

if length == 2 and num % 2 == 0:
    print("Парне двозначне число")
else:
    print("Ні")


# Задаємо конкретне число
num = int(input('введіть число'))
# Перевіряємо кратність
if num % 3 == 0 and num % 5 == 0: # найспецифічніша перевірка має пріоритет
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)




x = int(input("X: "))
y = int(input("Y: "))

if x == 0:
    print("X can`t be equal to zero")
    x = int(input("X: "))

result = y / x



if x >= 0:
    if y >= 0:  # x > 0, y > 0
        print("Перша чверть")
    else:  # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:  # x < 0, y > 0
        print("Друга чверть")
    else:  # x < 0, y < 0
        print("Третя чверть")



#-----------------------------

is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"

some_data = None
if some_data:
    msg = some_data
else:
    msg = "Не було повернено даних"



# Тернарні операції

is_nice = True
state = "nice" if is_nice else "not nice"

some_data = None
msg = some_data or "Не було повернено даних"


fruit = "apple"
match fruit:
    case "apple":
        print("This is an apple.")
    case "banana":
        print("This is a banana.")
    case "orange":
        print("This is an orange.")
    case _:
        print("Unknown fruit.")



point = (1, 0)
match point:
    case (0, 0):
        print("Точка в центрі координат")  
    case (0, y):
        print(f"Точка лежить на осі Y: y={y}")  
    case (x, 0):
        print(f"Точка лежить на осі X: x={x}") 
    case (x, y):
        print(f"Точка має координати:  x={x}, y={y}") 
    case _:
        print("Це не точка")

# Знак _ в шаблоні використовується як "заповнювач",
# що означає "будь-яке інше значення".

pets = ["dog", "fish", "cat"]
match pets:
    case ["dog", "cat", _]: 
        print("There's a dog and a cat.")
    case ["dog", _, _]:
        print("There's a dog.")
    case _:
        print("No dogs.")



fruit = 'apple'
for char in fruit:
    print(char)

alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char, end=" ") # a b c d e f g h i j k l m n o p q r s t u v w x y z


some_iterable = ["a", "b", "c"]
for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)


# Треба порахувати скільки символів в рядку та скільки пробілів в рядку.
# Зчитування рядка від користувача
user_input = input("Введіть рядок: ")
# Ініціалізація змінних для підрахунку символів та пробілів
total_chars = len(user_input)  # загальна кількість символів у рядку
space_count = 0  # кількість пробілів
# Підрахунок кількості пробілів
for char in user_input:
    if char == " ":
        space_count += 1
# Виведення результатів
print(f"Загальна кількість символів у рядку: {total_chars}")
print(f"Кількість пробілів у рядку: {space_count}")


k = 0
while k < 10:
    k = k + 1
print(k)


#умова циклу буде виконуватися завжди, адже True завжди буде True. 
# Це приклад нескінченного циклу. 
# Але через перевірку, що a >= 20, цей цикл завершиться
a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1

# Нескінченні цикли часто застосовуються там,
# де потрібно взаємодіяти з клієнтом, чекаючи введення від нього, 
# і завершується тільки при настанні деякої умови.


# echo скрипт, який виводить в консоль те,
# що ви введете, доки ви не введете рядок тексту exit
while True:
    user_input = input()
    print(user_input)
    if user_input == "exit":
        break


a = 0
while a < 6:
    a = a + 1
    if not a % 2:
        continue
    print(a)  # 1 3 5

# Оператори continue та break працюють тільки всередині одного циклу.
# В ситуації вкладених циклів немає способу вийти з усіх циклів одразу.
# використання continue або break поза циклом призводить до синтаксичної помилки.



my_list = [1, 2, None, 5, 8 ,None, None]
print(my_list.index(None)) # 2

while range(len(my_list)):
    if None not in my_list:
        break
    my_list.pop(my_list.index(None)) #видалить усі None

print(my_list) #[1, 2, 5, 8]



condition = True
start = 1
while condition:          # while start != 7:
    if start == 7:
        condition = False
    print("start ", end = '') #start start start start start start start Out of the loop
    start += 1
else:
    print("Out of the loop")



increment = 0
while increment <= 3:
    print(increment, end = '')
    increment += 1
else:
    print(0) #01230



string = "break statement"
for letter in string:
    print(letter, end = '')
    if letter == 'e' or letter == 's':
        break
    print(" Out of the loop")
'''виведе
b Out of the loop
r Out of the loop
e'''


for letter in string:
    print(letter, end = '')
    if letter == 'e' or letter == 's':
        continue
    print(" Out of the loop")
'''виведе
b Out of the loop
r Out of the loop
ea Out of the loop
k Out of the loop
  Out of the loop
st Out of the loop
a Out of the loop
t Out of the loop
em Out of the loop
en Out of the loop
t Out of the loop'''



for i in range(1, 10):
    if i % 2 == 0:
        print(f'{i} є парним числом.')
    else:
        print(f'{i} є непарним числом.')

for i in range(5):
    print(i) # 0 1 2 3 4

for i in range(2, 10):
    print(i)  # 2 3 4 5 6 7 8 9

for i in range(0, 10, 2):
    print(i) # 2 4 6 8


some_list = ["apple", "banana", "cherry"]
# enumerate() — це вбудована функція Python, 
# яка дозволяє одночасно отримувати індекс елемента і сам елемент під час перебору списку
for index, value in enumerate(some_list): 
    print(index, value) # 0 apple 1 banana 2 cherry



list1 = ["зелене", "стигла", "червоний"]
list2 = ["яблуко", "вишня", "томат"]
for number, letter in zip(list1, list2):
    print(number, letter)
# зелене яблуко
# стигла вишня
# червоний томат

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd', 'e']
for number, letter in zip(list1, list2):
    print(number, letter)
# 1 a
# 2 b
# 3 c



numbers = {
    1: "one",
    2: "two",
    3: "three"
}

for key in numbers:
    print(key) # 1 2 3

for key in numbers.keys():
    print(key) # 1 2 3

for val in numbers.values():
    print(val) # one two tree

for key, value in numbers.items():
    print(key, value) # 1 one 2 two 3 three



## Основні типи винятків у Python

# SyntaxError — синтаксична помилка.

# IndentationError —  у виділенні блоків інструкцій пробілами допущена помилка.

# TabError - якщо в одному файлі використовувати пробіли і табуляції для виділення блоків інструкцій.

# TypeError виникає, коли операція зі змінною цього типу неможлива.

# ValueError - коли тип операнда відповідний але значення таке, що операцію неможливо виконати.

#ZeroDivisionError — ділення на нуль.


val = 'a'
try:
    val = int(val)
except ValueError:
    print(f"val {val} is not a number")
else:
    print(val > 0)
finally:
    print("This will be printed anyway")


age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")









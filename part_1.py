################################

#Список — це впорядкований змінюваний контейнер даних.

my_list = list()
empty_list = []

my_list = [1, "Hello", 3.14]
my_list.remove("Hello")
print(my_list) # [1, 3.14]


#---------

number_list = [1, 2, 3, 4, 2, 2, 5, 2]
count_2 = number_list.count(2)
print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази

number_list.append(1000)
print(number_list) #[1, 2, 3, 4, 2, 2, 5, 2, 1000]

number_list.insert(1, 145)
print(number_list) # [1, 145, 2, 3, 4, 2, 2, 5, 2]

print(len(number_list)) #10



#-----

chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
print(c_ind) # Виведе 2

first_letter = chars[-4]
second_letter = chars[1]
print(first_letter) #a
print(second_letter) #b

chars[0] = 'f'
print(chars) #['f', 'b', 'c', 'd']
print(first_letter) #a !!!!!!!!

first_letter = chars[-4]
print(first_letter) #f !!!!!!

chars = ['a', 'b', 'c']
numbers = [1, 2]
chars.extend(numbers)
print(chars) #['a', 'b', 'c', 1, 2]

last = chars.pop(4)
print(last) #2
print(chars) #['a', 'c', 1]

chars_copy = chars.copy()
print(chars_copy) #['a', 'c', 1]


#-------
fruits = ["banana", "apple", "cherry", "blueberry"]
fruits.reverse()
print(fruits) #['blueberry', 'cherry', 'apple', 'banana']


#---


# метод sort() змінює сам список, на якому він був викликаний

nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()
print(nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

nums.sort(reverse=True)
print(nums)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
words.sort(key=len)
print(words)  # Виведе ['apple', 'banana', 'cherry']

# метод sorted() повертає новий відсортований об'єкт, залишаючи вихідний об'єкт без змін.
# можна використовувати з будь-якою колекцією, незалежно від того, чи є вихідний об'єкт змінним.

nums = [3, 1, 4, 1, 5, 9, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]

sorted_nums_desc = sorted(nums, reverse=True)
print(sorted_nums_desc)  # Виведе [9, 5, 4, 3, 2, 1, 1]

words = ["banana", "apple", "cherry"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']


#########################

#Словник — це контейнер, який зберігає пари ключ-значення. 
# Ключем може бути будь-який незмінний тип даних Python (число, рядок, кортеж тощо).
# Значенням словника може бути будь-який тип даних Python

my_dict = {}

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict) #{'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

del my_dict["age"]
print(my_dict) #{'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'} 

print("name" in my_dict) #True
print("age" in my_dict) #False

email = my_dict.pop("email")
print(email) #lice@example.com
print(my_dict) #{'name': 'Alice', 'city': 'New York'} 

my_dict.update({'name': 'Katy', "email": "alice@example.com", "age": 13})
print(my_dict) #{'name': 'Katy', 'city': 'New York', 'email': 'alice@example.com', 'age': 13}

new_dict = my_dict.copy()
print(new_dict) #{'name': 'Katy', 'city': 'New York', 'email': 'alice@example.com', 'age': 13}

my_dict.clear()
print(my_dict) #{}


my_dict = {"name": "Alice", "age": 25}
age = my_dict.get("age")  # Поверне 25
name = my_dict["name"]  # Поверне 'Alice'
gender = my_dict.get("gender")  # Поверне None, оскільки "gender" немає в словнику
# gender = my_dict["gender"]  # Викличе KeyError !!!! код далі не працюватиме!!!!!
#краще використовуй метод get() для отримання значення за ключем зі словника.




#####################################################

# Множини — це неврегульований контейнер, який містить тільки унікальні елементи. 
# У множину можна додавати тільки незмінні типи даних.

empty_set = set()

a = set('hello')
b = {1, 2, 3, 4, 5}

# використовуються, коли потрібно забезпечити унікальність елементів,
# для видалення дублікатів зі списку
# виконати швидкі перевірки на наявність елемента.

lst = [1, 2, 3, 1, 2, 2, 3, 4, 1]
d_lst = set(lst)
print(d_lst) #{1, 2, 3, 4}

lst=list(d_lst)
print(lst) #[1, 2, 3, 4]

numbers = {1, 2, 3}
numbers.add(4)
print(numbers)  # {1, 2, 3, 4}

numbers.remove(3)
#numbers.remove(9) #KeyError
print(numbers)  # {1, 2, 4}

numbers.discard(2)
numbers.discard(9) # видаляє елемент із множини і не викликає виняток, якщо його немає
print(numbers)  # {1, 4}



#-------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a.intersection(b))  # {3}
print(a & b)  # {3}

print(a.difference(b))  # {1, 2}
print(a - b)  # {1, 2}

print(a.symmetric_difference(b))  # {1, 2, 4, 5}
print(a ^ b)  # {1, 2, 4, 5}

print(a.union(b))  # {1, 2, 3, 4, 5}
print(a | b)  # {1, 2, 3, 4, 5}



#-----------------
#після створення замороженої множини ви не можете додати або видалити елементи з неї
# Заморожені множини можуть використовуватися в якості ключів у словниках або як елементи інших множин, 
# тому що вони є хешованими (і, отже, незмінними).

my_frozenset = frozenset([1, 2, 3, 4, 5])

a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])

union = a | b  # Об'єднання множин
intersection = a & b  # Перетин множин
difference = a - b  # Різниця множин
symmetric_difference = a ^ b  # Симетрична різниця

print(union)  # frozenset({1, 2, 3, 4, 5})
print(intersection)  # frozenset({3})
print(difference)  # frozenset({1, 2})
print(symmetric_difference)  # frozenset({1, 2, 4, 5})



############################################################

#Кортежі — незмінні. Після створення кортежу, не можна змінити його елементи, 
# не можна додавати/видаляти/переставляти елементи.
# корисні в якості ключів словників, або як елементи множини
# для зберігання набору констант або коли функція повертає кілька значень.

my_tuple = tuple() # або
my_tuple = ()

my_tuple = (1, 2, 3)
my_tuple = (1, "Hello", 3.14)
my_tuple = 1, "Hello", 3.14 # Операція упакування кортежу

my_tuple = (1,) # !!!!!! Якщо кортеж з одним елементом, не забудьте поставити кому

first_item = my_tuple[0]  # Отримати перший елемент

points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
} # набір точок на площині (кортежі) як ключі у словнику




########################################################

#Рядок — це незмінна впорядкована послідовність символів у деякому кодуванні.
#  За замовчуванням використовується кодування UTF-8

game_string = 'My favorite "Game"'

s = "Hello world!"
print(s[0])# H
print(s[-1])# !
#s[0] = "Q"# Тут буде викликано виняток (помилка) TypeError

s = "Hello" 
print(s.upper()) # HELLO
print(s.lower())  # hello

s = "hello world".capitalize() 
print(s) # Hello world

s = "hello world".title()  
print(s) # Hello World

s = "Bill Jons"
print(s.startswith("Bi"))  # True

s = "hello.jpg"
print(s.endswith("jpg"))  # True

# чи складається рядок тільки з цифр, літер, пробілів?
"123".isdigit()  # True
"hello".isalpha()  # True
" ".isspace()  # True

# Просте форматування рядка
name = 'John'
print('Hello, {}!'.format(name))

# Форматування з декількома аргументами
age = 25
print('Hello, {}. You are {} years old.'.format(name, age))

# Використання іменованих аргументів
print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# Використання індексів для вказівки порядку аргументів
print('Hello, {1}. You are {0} years old.'.format(age, name))


# Зрізи (slices) у Python — це потужний механізм для доступу до частин 
# послідовностей, таких як рядки, списки та кортежі.

# послідовність[початок:кінець:крок]

s = "Hello, World!"
first_five = s[:5]
print(first_five)  # Hello

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:10:2] # [1, 3, 5, 7, 9]
odd_numbers = numbers[::2]  # [1, 3, 5, 7, 9]

even_numbers = numbers[1:10:2] # [2, 4, 6, 8, 10]
even_numbers = numbers[1::2] # [2, 4, 6, 8, 10]

three_numbers = numbers[2:10:3] # [3, 6, 9]
three_numbers = numbers[2::3] # [3, 6, 9]

reverse_numbers = numbers[::-1]
print(reverse_numbers) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

copy_numbers = numbers[:]
print(copy_numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Модуль collections

# namedtuple

# Створення іменованого кортежу дозволяє виконувати доступ 
# до елементів списку за іменем, а не тільки за індексом
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
# Створення екземпляра Point
p = Point(11, y=22)
# Доступ до елементів
print(p.x)  # 11
print(p.y)  # 22


person = ('Mick', 'Nitch', 35, 'Boston', '01146') # кортеж
# Створення іменованого кортежу Person
Person = namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])
# Створення екземпляра Person
person = Person('Mick', 'Nitch', 35, 'Boston', '01146')
# Виведення різних атрибутів іменованого кортежу
print(person.first_name)  # Mick   
print(person.post_index) # 01146
print(person.age) # 35       
print(person[3]) # Boston   


Cat = namedtuple('Cat', ['nickname', 'age', 'owner'])
cat = Cat('Simon', 4, 'Krabat')
print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}') #This is a cat Simon, 4 age, his owner Krabat


# Counter

# коли потрібно швидко підрахувати кількість окремих елементів у колекції
# функціонує як словник, де ключами є елементи, а значеннями - їх кількість у колекції.
from collections import Counter

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = Counter(student_marks)
print(mark_counts) # Counter({4: 4, 6: 3, 1: 3, 2: 2, 7: 2, 3: 2, 5: 2})

# most_common() повертає список елементів та їх частоту, починаючи з тих, які зустрічаються найчастіше
print(mark_counts.most_common()) # [(4, 4), (6, 3), (1, 3), (2, 2), (7, 2), (3, 2), (5, 2)]
print(mark_counts.most_common(1)) # [(4, 4)]
print(mark_counts.most_common(2)) # [(4, 4), (6, 3)]


letter_count = Counter("banana")
print(letter_count) # Counter({'a': 3, 'n': 2, 'b': 1})


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_count = Counter(words)
# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")


# defaultdict

# дозволяє призначити значення за замовчуванням для ключів, які ще не існують у словнику
# у звичайному словнику Python спроба доступу до ключа, якого не існує, викликає виняток KeyError
from collections import defaultdict

# Створення defaultdict з list як фабрикою за замовчуванням
d = defaultdict(list)
# Додавання елементів до списку для кожного ключа
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d) # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]}) 
#
# ви повинні передати функцію, яка повертає значення за замовчуванням для нових ключів.
# Це може бути будь-який об'єкт, який може бути викликаний, наприклад, int, list, set 
# або навіть ваша функція.
d = defaultdict(int)
# Збільшення значення для кожного ключа
d['a'] += 1
d['b'] += 1
d['a'] += 1
print(d)  # defaultdict(<class 'int'>, {'a': 2, 'b': 1})


words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
grouped_words = {}
for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)
print(grouped_words) # {'a': ['apple', 'appendix'], 'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}
# або
grouped_words = defaultdict(list) # задати значенням за замовчуванням порожній список
for word in words:
    char = word[0]
    grouped_words[char].append(word)
print(dict(grouped_words)) # {'a': ['apple', 'appendix'], 'z': ['zoo'], 'l': ['lion', 'lama'], 'b': ['bear', 'bet'], 'w': ['wolf']}



'''Стек - це структура даних у програмуванні, яка дозволяє здійснювати операції 
вставки і вилучення даних за принципом "Останнім прийшов - першим вийшов" 
(LIFO - Last In, First Out).'''
# Створення стеку
def create_stack():
    return []

# Перевірка на порожнечу
def is_empty(stack):
    return len(stack) == 0

# Додавання елементу
def push(stack, item):
    stack.append(item)

# Вилучення елементу
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Стек порожній")

# Перегляд верхнього елемента
def peek(stack):
    if not is_empty(stack):
        return stack[-1]
    else:
        print("Стек порожній")


stack = create_stack()
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(peek(stack))  # c
print(pop(stack))  # c




'''Черга (queue) у програмуванні — це абстрактна структура даних, яка діє за принципом
"першим прийшов – першим вийшов" (FIFO: First In, First Out). 
Елементи додаються (enqueue) на один кінець структури та видаляються (dequeue) з іншого кінця.
Черги, застосовують для задач, де елементи повинні бути оброблені в порядку їх надходження.'''

# deque

from collections import deque
# Створення черги
queue = deque()
# Enqueue: Додавання елементів
queue.append('a')
queue.append('b')
queue.append('c')
print("Черга після додавання елементів:", list(queue)) #  Черга після додавання елементів: ['a', 'b', 'c']
# Dequeue: Видалення елемента
print("Видалений елемент:", queue.popleft()) # Видалений елемент: a
print("Черга після видалення елемента:", list(queue)) # Черга після видалення елемента: ['b', 'c']
# Peek: Перегляд першого елемента
print("Перший елемент у черзі:", queue[0]) # Перший елемент у черзі: b
# IsEmpty: Перевірка на порожнечу
print("Чи черга порожня:", len(queue) == 0) # Чи черга порожня: False
# Size: Розмір черги
print("Розмір черги:", len(queue)) # Розмір черги: 2


'''Двостороння черга, Deque (скорочення від "double-ended queue"), є типом структури даних, 
яка дозволяє вставляти та видаляти елементи з обох кінців.'''
# append(x) - додає елемент x в кінець черги.
# appendleft(x) - додає елемент x на початок черги.
# pop() - видаляє та повертає елемент з правого кінця черги. Якщо черга порожня, викидає виняток IndexError.
# popleft() - видаляє та повертає елемент з лівого кінця черги. Якщо черга порожня, викидає виняток IndexError.

d = deque()
d.append('middle')  # Додаємо 'middle' в кінець черги
d.append('last')    # Додаємо 'last' в кінець черги
d.appendleft('first')  # Додаємо 'first' на початок черги
print("Черга після додавання елементів:", list(d)) # Черга після додавання елементів: ['first', 'middle', 'last']
print("Видалений останній елемент:", d.pop()) # Видалений останній елемент: last
print("Видалений перший елемент:", d.popleft()) # Видалений перший елемент: first
print("Черга після видалення елементів:", list(d)) # Черга після видалення елементів: ['middle']

# обмежити розмір Deque
d = deque(maxlen=5)
for i in range(20):
    d.append(i) # нові елементи витісняють старіші, але розмір залишається незмінним
print(d) # deque([15, 16, 17, 18, 19], maxlen=5)


'''задача — розподілити ці завдання таким чином, щоб швидкі завдання виконувалися першими'''
# Список завдань, де кожне завдання - це словник
tasks = [
    {"type": "fast", "name": "Помити посуд"},
    {"type": "slow", "name": "Подивитись серіал"},
    {"type": "fast", "name": "Вигуляти собаку"},
    {"type": "slow", "name": "Почитати книгу"}
]
# Ініціалізація черги завдань
task_queue = deque()
# Розподіл завдань у чергу відповідно до їх пріоритету
for task in tasks:
    if task["type"] == "fast":
        task_queue.appendleft(task)  # Додавання на високий пріоритет
        print(f"Додано швидке завдання: {task['name']}")
    else:
        task_queue.append(task)  # Додавання на низький пріоритет
        print(f"Додано повільне завдання: {task['name']}")
# Виконання завдань
while task_queue:
    task = task_queue.popleft()
    print(f"Виконується завдання: {task['name']}")

'''Додано швидке завдання: Помити посуд
Додано повільне завдання: Подивитись серіал
Додано швидке завдання: Вигуляти собаку
Додано повільне завдання: Почитати книгу
Виконується завдання: Вигуляти собаку
Виконується завдання: Помити посуд
Виконується завдання: Подивитись серіал
Виконується завдання: Почитати книгу'''



# Decimal 

# це клас у модулі decimal, який забезпечує точну арифметику з дійсними числами
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3")) # True
print(Decimal("0.1") + Decimal("0.2")) # 0.3

# Точність обчислень з Decimal контролюється через контекст. 
# Можна налаштувати загальну точність для всіх обчислень Decimal.
from decimal import Decimal, getcontext

getcontext().prec = 6
print(Decimal("1") / Decimal("7")) # 0.142857

getcontext().prec = 8
print(Decimal("1") / Decimal("7")) # 0.14285714
# getcontext встановлює кількість значущих цифр. 
# А значущими числами можуть бути і цифри перед комою.
''' Визначення значущих цифр:
Усі ненульові цифри є значущими: 1, 2, 3, 4, 5, 6, 7, 8, 9.
Нулі між ненульовими цифрами значущі: 102, 2005, 50009.
Провідні нулі ніколи не бувають значущими: 0,02; 001,887; 0,000515.
В числі з десятковою або без десяткової коми знаходяться знакові нулі 
(праворуч від останньої ненульової цифри) за умови, якщо вони обґрунтовані точністю їх використання: 389,000; 2,02000; 5,400; 57,5400.'''
getcontext().prec = 6
print(Decimal("233") / Decimal("7")) # 33.2857

'''Якщо ми потребуємо саме округлення чисел, нам необхідно використовувати метод quantize.
Метод quantize використовується для встановлення точності числа Decimal, 
заснованої на іншому числі Decimal, яке використовується як шаблон.
Наприклад, якщо ви хочете округлити число до двох знаків після коми, 
ви використовуєте Decimal об'єкт з двома нулями після коми як шаблон.'''

''' Його використання є критично важливим у фінансових застосунках, бухгалтерському обліку'''

import decimal
from decimal import Decimal, ROUND_DOWN
# Вихідне число Decimal
number = Decimal('3.14159')
# Встановлення точності до двох знаків після коми
rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)
print(rounded_number) # 3.14
 

number = Decimal("1.45")
# Округлення за замовчуванням до одного десяткового знаку
print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0"))) # 1.4

# Округлення вверх при нічиї (ROUND_HALF_UP)
print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP)) # 1.5

# Округлення вниз (ROUND_FLOOR)
print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR)) # 1.4

# Округлення вверх (ROUND_CEILING)
print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING)) # 1.5

# Округлення до трьох десяткових знаків за замовчуванням
print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000"))) # 3.142




# Генератори
# функції з декількома точками входу

# Оператор yield повертає управління потоком виконання програмою з тіла функції. 
# Але, на відміну від return, yield при наступному зверненні не розпочинає виконання функції з початку,
# а продовжує з місця зупинки функції.

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
# Використання next()
print(next(gen))  # Виведе 1
print(next(gen))  # Виведе 2
print(next(gen))  # Виведе 3
# Щоб кожен раз не використовувати try except для контролю винятку StopIteration 
# найчастіше генератори використовуються безпосередньо в циклах for ...

def count_down(start):
    while start > 0:
        yield start
        start -= 1
for number in count_down(5):
    print(number)


from pathlib import Path
   
def read_lines(file_path):
    current_directory = Path(__file__).parent
    with open(current_directory / file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()
# Використання генератора для читання рядків з файлу
for line in read_lines("my_file.txt"):
    print(line)
# Усередині функції read_lines цикл for ітерується по кожному рядку у файлі. 
# Ключове слово yield використовується для повернення кожного рядка файлу. 
# Попередньо кожен рядок оброблено методом strip(), щоб видалити пробіли та 
# символи нового рядка по краях.
# Це дуже ефективно з точки зору використання пам'яті, особливо для великих даних. 
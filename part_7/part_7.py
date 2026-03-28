'''
Функтори — це об'єкти, які можна викликати та передавати їм аргументи.
за допомогою реалізації спеціального магічного методу __call__ для класу
'''
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other

# Створення екземпляра функтора
double = Multiplier(2)
triple = Multiplier(3)
# Метод __call__ дозволяє екземплярам Multiplier викликатися як функції, які множать передане їм 
# значення на фактор, вказаний при створенні екземпляру

# Виклик функтора
print(double(5))  # 10
print(triple(3))  # 9

#--------------------------------------------

'''Розглянемо функтор зі станом. Він буде використовувати свій внутрішній стан 
для підрахунку кількості разів, коли його викликали.'''

class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1

counter = Counter()
counter()
counter()
print(f"Викликано {counter.count} разів") # Викликано 2 разів

#-------------------------------------------


'''Розглянемо функтор який використовує внутрішній стан та додаткові параметри для вирішення, 
яку дію виконати при виклику. Цей функтор приймає параметри при ініціалізації, які потім 
використовуються для налаштування його поведінки.'''

class SmartCalculator:
    def __init__(self, operation='add'):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == 'add':
            return a + b
        elif self.operation == 'subtract':
            return a - b
        else:
            raise ValueError("Невідома операція")

add = SmartCalculator('add')
print(add(5, 3))  # 8

subtract = SmartCalculator('subtract')
print(subtract(10, 7))  # 3


'''Ітератор в Python — це об'єкт, який дозволяє нам послідовно перебирати елементи будь-якого об'єкта 
ітерації (наприклад, списку, кортежу, словника) без потреби використання індексів. Він реалізує методи
 __iter__() та __next__() та дозволяє перебирати елементи послідовності, не завантажуючи всю 
 послідовність у пам'ять.

Метод __iter__() повертає сам ітератор, а метод __next__() повертає наступний елемент об'єкта ітерації.
Коли елементи ітератора закінчуються, має бути викинуто виняток StopIteration, що сигналізує про 
завершення ітерації.

Оскільки ітератор дозволяє нам перебирати елементи контейнера за допомогою циклу for-in, 
то основна ідея полягає в тому, що ітератор зберігає поточний стан перебору, дозволяючи вам 
отримувати наступний елемент за допомогою методу __next__().
'''
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current

if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count) # 4 3 2 1 0

'''Генератор - це спрощений спосіб створення ітераторів. Функція стає генератором, коли містить 
вираз yield. Генератор автоматично реалізує методи __iter__() та __next__().'''

def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1

# Використання генератора
for count in count_down(5):
    print(count) # 4 3 2 1 0

#-------------------------------------


from random import randint

class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)

if __name__ == '__main__':
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end=' ') # 20 9 6 20 13 


'''Щоб перетворити ітератор на генератор, ми можемо використати функцію з ключовим словом yield 
замість класу з методами __iter__() та __next__(). Генератор автоматично веде облік свого стану 
в місці кожного виклику yield і відновлює виконання з цього місця при наступному виклику.'''

from random import randint

def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1

if __name__ == '__main__':
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')


'''Генератори особливо ефективні коли потрібно обробляти великі обсяги даних або виконувати 
складні обчислення з мінімальним навантаженням на пам'ять.

Метод send() використовується для взаємодії з генератором шляхом надсилання значення у генератор, 
яке потім може бути використане як результат виразу yield. Це дозволяє генератору не лише виробляти 
дані, але й обробляти зовнішні дані на кожній ітерації.
'''

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"

gen = my_generator()
print(next(gen))  # Ready
print(gen.send("Hello"))  # Received: Hello


'''Коли генератору більше не потрібно виробляти значення, його можна закрити за допомогою 
методу close(). При цьому в генераторі викликається виключення GeneratorExit, яке можна перехопити 
для виконання якихось дій перед закриттям генератора.'''

def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Working
gen.close()  # Generator is being closed

#-----------------------------


def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()

# Ініціалізація генератора
next(gen)  # Або gen.send(None), щоб стартувати

# Відправлення числа в генератор і отримання результату
result = gen.send(10)  # Повинно повернути 100
print(f"Square of 10: {result}")

# Перехід до наступного очікування
next(gen)

# Відправлення іншого числа
result = gen.send(5)  # Повинно повернути 25
print(f"Square of 5: {result}")

# Закриття генератора
gen.close()

#-----------------------------------------------------------


def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages) # Looking for hello Generator closed
    # ['Line accepted: hello world', 'Line accepted: another hello world line', 'Line accepted: hello again']



'''Створення власного менеджера контексту в Python - це спосіб керування ресурсами, такими як файли,
 з'єднання з базою даних та інше, забезпечуючи їх автоматичне відкриття та закриття. Менеджер контексту 
 гарантує, що ресурси будуть коректно звільнені після завершення блоку коду, навіть якщо в процесі 
 виконання виникне виключення.
Об'єкти контекстних менеджерів слугують для управління оператором with ... as ...: так само як 
ітератори управляють оператором циклу for-in.
Для створення власного менеджера контексту необхідно реалізувати клас з магічними методами 
__enter__ та __exit__. Метод __enter__ викликається на початку блоку with, коли інтерпретатор заходить
 у контекст і те, що він поверне, буде записано в змінну після as. Метод __exit__ викликається після 
 завершення виконання блоку with, незалежно від того, виникло виключення чи ні.
'''
# class MyContextManager:
#     def __enter__(self):
#         # Ініціалізація ресурсу
#         print("Enter the block")
#         return self  # Може повертати об'єкт

#     def __exit__(self, exc_type, exc_value, traceback):
#         # Звільнення ресурсу
#         print("Exit the block")
#         if exc_type:
#             print(f"Error detected: {exc_value}")
#         # Повернення False передає виключення далі, True - поглинає виключення.
#         return False

# # Використання власного менеджера контексту
# with MyContextManager() as my_resource:
#     print("Inside the block")
#     raise Exception("Something went wrong")

# #--------------------------------------------------

# def __exit__(self, exc_type, exc_val, exc_tb):
#     # Звільнення ресурсів
#     # exc_type: тип виключення
#     # exc_val: значення виключення
#     # exc_tb: трасування стека виключення
#     return False  # Якщо True, виключення буде придушено, інакше - прокинуто далі

# ''' Python дозволяє створювати менеджери контексту за допомогою генераторів і 
# декоратора contextmanager з модуля contextlib. Це спрощує створення менеджерів контексту, 
# особливо коли вони використовуються для одноразових або простих задач без необхідності 
# визначати клас з методами __enter__ та __exit__'''

# from contextlib import contextmanager

# @contextmanager
# def my_context_manager():
#     # Ініціалізація ресурсу
#     print("Enter the block")
#     try:
#         yield  # Місце виконання блоку `with`
#     except Exception as e:
#         # Обробка виключень
#         print(f"Error detected: {e}")
#         # Можна ре-підняти виключення або вирішити його тут
#         raise
#     finally:
#         # Звільнення ресурсу
#         print("Exit the block")

# # Використання
# with my_context_manager():
#     print("Inside the block")
#     raise Exception("Something went wrong")



'''Створимо клас FileManager, який призначений для роботи з файлами та логування процесу відкриття 
та закриття файлу.'''

class FileManager:
    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Відкриваємо файл", self.filename)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Завершення блоку with")
        if self.opened:
            print("Закриваємо файл", self.filename)
        self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileManager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n') #Закриваємо файл new_file.txt  Завершення блоку with  Hello world! The end

#------------------------------------------------

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode='w', encoding='utf-8'):
    print("Відкриваємо файл", filename)
    file = open(filename, mode, encoding=encoding)
    try:
        yield file
    finally:
        print("Закриваємо файл", filename)
        file.close()
        print("Завершення блоку with")


if __name__ == '__main__':
    with file_manager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')


'''Створимо контекстний менеджер, який буде управляти відкриттям та закриттям файлу з додатковим 
логуванням. Наш контекстний менеджер managed_resource буде вимірювати час виконання операцій з файлом 
та логувати дії відкриття і закриття файлу разом з тривалістю їх виконання.
'''

from contextlib import contextmanager
from datetime import datetime


@contextmanager
def managed_resource(*args, **kwargs):
    log = ''
    timestamp = datetime.now().timestamp()
    msg = f'{timestamp:<20}|{args[0]:^15}| open \n'
    log += msg
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        diff = datetime.now().timestamp() - timestamp
        msg = f'{timestamp:<20}|{args[0]:^15}| closed {round(diff, 6):>15}s \n'
        log += msg
        file_handler.close()
        print(log)


with managed_resource('new_file.txt', 'r') as f:
    print(f.read())
# 1774727554.57883    | new_file.txt  | open
# 1774727554.57883    | new_file.txt  | closed        0.004997s

'''Це може бути досить корисно при діагностиці та аналізі продуктивності нашої програми.'''
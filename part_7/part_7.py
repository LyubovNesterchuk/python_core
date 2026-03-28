''' в мові програмування Python практично кожен елемент можна розглядати як об'єкт.

Магічні методи відповідають за визначену поведінку об'єктів при використанні операторів або 
інших синтаксичних конструкцій.
вираз a + b на низькому рівні трансформується в виклик a.__add__(b), перетворюючи стандартну операцію 
додавання на виклик методу, який може бути перевизначений за бажанням розробника. 

метод __init__ відповідає за ініціалізацію об'єкта. 
Коли ви створюєте об'єкт класу, то спочатку створюється порожній об'єкт, який містить лише обов'язкові 
службові атрибути. Після того як об'єкт створено, автоматично викликається метод __init__, 
який ми можемо модифікувати під наші потреби.
'''
class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()  
        
        # Приклад логування
        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}")

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'

    def __check_adulthood(self) -> bool:
        return self.age >= 18

bill = Human('Bill')
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")

jill = Human('Jill', 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")


'''Метод __repr__ призначений для створення офіційного рядкового представлення об'єкта. 
Розробники використовують його для однозначного ідентифікування об'єкта або навіть для відтворення 
об'єкта в іншому місці коду.'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)

'''ви можете використовувати вираз, повернутий методом __repr__, як Python команду для створення 
нового об'єкта, який буде мати ті самі характеристики, що й оригінальний об'єкт. Ця особливість 
особливо корисна для налагодження, де ви можете легко відтворити об'єкти на основі їхнього __repr__ представлення.'''

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

original_point = Point(2, 3)
print(repr(original_point))  # Point(x=2, y=3)

# Використання рядка, повернутого __repr__, для створення нового об'єкта
new_point = eval(repr(original_point))
print(new_point) # Point(x=2, y=3)

'''Функція eval() використовується для виконання рядкового виразу як коду. Вона приймає рядок і виконує
 його як вираз Python, повертаючи результат виконання цього виразу. Коли метод __repr__ класу повертає рядок, 
 його можна передати до eval(). Ідея полягає в тому, щоб виклик eval() з результатом __repr__ створив 
 новий об'єкт, ідентичний оригіналу.'''

'''Метод __str__ призначений для повернення рядкового представлення об'єкта, яке має бути читабельним 
і зрозумілим для людини. Коли ви викликаєте функцію str() для об'єкта або друкуєте об'єкт за допомогою print(),
 Python автоматично використовує метод __str__ вашого класу.'''

class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print(human)


'''
Квадратні дужки дозволяють нам звертатися до елементів послідовності за індексом або до елементів словника за ключем.

Метод __getitem__ визначає, як об'єкт класу повинен вести себе при доступі до його елементів за допомогою 
індексу або ключа. Він приймає ключ або індекс як аргумент і повинен повертати значення, асоційоване з цим ключем 
або індексом.

Метод __setitem__ визначає, як об'єкт повинен поводити себе при присвоєнні значення елементу за певним індексом 
або ключем. Він приймає два аргументи: ключ (або індекс) та значення, яке потрібно асоціювати з цим ключем.'''


class SimpleDict: # використовує внутрішній приватний словник __data для зберігання своїх елементів
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  #Boris
print(simple_dict['age'])  #Key not found

#------------------------
'''вбудована функція ->enumerate([10, 20, 30], start=1)->(1, 10), (2, 20), (3, 30)
те ж саме, що написати вручну:
i = 0
for el in [10, 20, 30]:
    i += 1
'''

'''керування температурою в приміщенні, де значення температури повинні бути обмежені мінімальним 
та максимальним порогом'''

class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]): # повертає послідовність пар (0, 20) (1, 22) (2, 25) (3, 27)
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)
#проба встановити значення поза дозволеним діапазоном призводить до виведення помилки
    print(temperatures) # Value 27 must be between 18 and 26     [20, 22, 25]


    #--------------------------------------------

from collections import UserList

class BoundedList(UserList):
    def __init__(self, min_value: int, max_value: int, initial_list=None):
        super().__init__(initial_list if initial_list is not None else [])
        self.min_value = min_value
        self.max_value = max_value
        self.__validate_list()

    def __validate_list(self):
        for item in self.data:
            self.__validate_item(item)

    def __validate_item(self, item):
        if not (self.min_value <= item <= self.max_value):
            raise ValueError(f"Item {item} must be between {self.min_value} and {self.max_value}")

    def append(self, item):
        self.__validate_item(item)
        super().append(item)

    def insert(self, i, item):
        self.__validate_item(item)
        super().insert(i, item)

    def __setitem__(self, i, item):
        self.__validate_item(item)
        super().__setitem__(i, item)

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.data)
    
    def __getitem__(self, index):
        # Додати спеціальну логіку тут, наприклад, логування або перевірку
        print(f"Accessing item at index {index}")
        # Викликати оригінальний метод __getitem__
        return super().__getitem__(index)  


if __name__ == '__main__':
    temperatures = BoundedList(18, 26, [19, 21, 22])
    print(temperatures)

    for el in [20, 22, 25, 27]:
        try:
            temperatures.append(el)
        except ValueError as e:
            print(e)

    print(temperatures) # [19, 21, 22]   Item 27 must be between 18 and 26     [19, 21, 22, 20, 22, 25]



    









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


'''методи для перевизначення математичних операторів:
__add__(self, other) для оператора +
__sub__(self, other) для оператора -
__mul__(self, other) для оператора *
__truediv__(self, other) для оператора /
__floordiv__(self, other) для оператора цілочисельного ділення //
__mod__(self, other) для оператора залишку від ділення %
__pow__(self, other) для оператора * піднесення до степеня'''
    

from collections import UserDict

class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)

    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)

if __name__ == '__main__':
    d1 = MyDict({1: 'a', 2: 'b'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d3 = d1 + d2
    print(d3) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

    d4 = d3 - d2
    print(d4) # {1: 'a', 2: 'b'}



#--------------------------

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Сума: {num1 + num2}")
    print(f"Різниця: {num1 - num2}")
    print(f"Добуток: {num1 * num2}")


#------------------------------------------------

'''реалізуємо векторне множення, де результатом є скалярний добуток векторів'''

from collections import UserList

class MulArray(UserList):
    def __init__(self, *args):
        self.data = list(args)

    def __mul__(self, other):
        return self.__scalar_mul(other)
    
    def __rmul__(self, other):
        return self.__scalar_mul(other) 
    
    def __scalar_mul(self, other):
        result = 0
        for i in range(min(len(self.data), len(other))):
            result += self.data[i] * other[i]
        return result

if __name__ == '__main__':
    vec1 = MulArray(1, 2, 3)
    vec2 = MulArray(3, 4, 5)

    print(vec1 * vec2) # 26
    print(vec1 * [1, 2, 3]) #14
    print([1, 1, 1] * vec2) #12


'''операції порівняння, як і інші оператори, мають свої "магічні" методи:

__eq__(self, other) — визначає поведінку під час перевірки на відповідність (==).
__ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
__lt__(self, other) — визначає поведінку під час перевірки на менше <.
__gt__(self, other) — визначає поведінку під час перевірки на більше >.
__le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
__ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.
'''

''' клас Rectangle, який представляє прямокутник з двома властивостями: 
шириною width і висотою height. 
порівнювати прямокутники на основі розміру їх площі.'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):# є прийнятою практикою, коли ви стикаєтеся 
            #з ситуацією, де ваш метод не знає, як порівнювати об'єкт з іншим типом об'єкта
            return NotImplemented 
        return self.area() == other.area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)
    print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
    print(rect1 == rect3)  # True: площі рівні
    print(rect1 != rect2)  # True: площі не рівні
    print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
    print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
    print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
    print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3

    #-----------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y

if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True


'''У мові програмування Python, поля - це змінні, які зберігають інформацію про стан об'єкта.
Доступ до цих полів та їх модифікація зазвичай відбувається безпосередньо, але іноді необхідно 
контролювати цей процес, наприклад, для валідації даних або інкапсуляції. Для цього існують 
спеціальні методи які називають гетерами та сетерами. 
Гетери дозволяють отримати значення поля. Вони використовуються, коли доступ до поля потребує якоїсь 
додаткової обробки або коли безпосередній доступ до поля не бажаний з міркувань інкапсуляції.
Наприклад, якщо потрібно завжди повертати значення поля у вигляді рядка, навіть якщо воно зберігається 
як число.
Сетери дозволяють встановити значення поля, використовуються для валідації даних, які намагаються 
присвоїти полю. Наприклад, якщо ми маємо поле, який повинно приймати значення лише додатні числа, 
можна в сетері додати перевірку, яка буде викидати виняток або повертати помилку, якщо намагатися 
присвоїти йому від'ємне число.
Вбудований декоратор @property робить метод класу доступним як поле, тобто його можна буде викликати
без дужок.  Для створення сетера для того ж поля, що і гетер, використовується
декоратор @property.setter, який застосовується до методу з тим же ім'ям, що і властивість.'''

class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    #person.age = -5


#---------------------------------------------

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"

if __name__ == "__main__":
    p = Person("Boris", 34, True, False)
    print(p.is_admin)  # Використовуємо геттер
    p.is_admin = True  # Використовуємо сеттер
    print(p.is_admin)

#---------------------------------------------

class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()
p.value = 1
print(p.value)  # 1
p.value = -1  # Only numbers greater zero accepted
p._PositiveNumber__value = -1
print(p.value)  # -1





'''Статичні методи використовують декоратор @staticmethod і є методами, які не мають доступу до 
екземпляру класу тобто змінної self, з якого вони були викликані. Це означає, що статичні методи 
не можуть змінювати стан об'єкта або класу, але вони можуть бути корисними для виконання деяких 
операцій, які не залежать від стану об'єкта. Статичні методи можна розглядати як "допоміжні" функції,
які мають логічний зв'язок із класом, але не потребують доступу до його атрибутів або методів.
'''

class Geometry:
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius ** 2

print(Geometry.area_of_circle(5))  # 78.53975


'''Класові методи використовують декоратор @classmethod і мають доступ до самого класу через 
параметр cls, який автоматично передається Python. Це означає, що класові методи можуть змінювати 
стан класу або викликати інші класові методи. '''

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)
# дозволяє створювати екземпляри Employee, розбираючи рядок на поля. Метод використовує параметр cls 
# для створення нового екземпляра, гарантуючи, що він може бути успішно використаний навіть 
# у класах-нащадках. В нашому прикладі cls це буде сам клас Employee.
employee_info = "John Doe,Manager"
john_doe = Employee.from_string(employee_info)

print(john_doe.name)  # Виведе: John Doe
print(john_doe.position)  # Виведе: Manager


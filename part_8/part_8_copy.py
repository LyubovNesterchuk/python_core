'''серіалізація - це процес перетворення об'єкта у потік байтів для зберігання або 
передачі. Десеріалізація - зворотний процес, коли потік байтів перетворюється назад 
у об'єкт. Але не всі об'єкти Python можна серіалізувати. Наприклад, не можна 
серіалізувати файловий дескриптор або системний ресурс.
У такій ситуації можна скористатися магічними методами, які управляють серіалізацією 
та десеріалізацією за допомогою pickle.'''

import pickle

class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        self.is_active = False   # Цей атрибут ми не збираємось серіалізувати

    def __getstate__(self):
        state = self.__dict__
        del state['is_active']  # Видаляємо is_active з серіалізованого стану
        return state

    def __setstate__(self, state):
        self.__dict__.update(state) # Відновлюємо об'єкт при десеріалізації
        self.is_active = False      # Задаємо значення is_active за замовчуванням

robot = Robot("Robo1", 100)                          # Створення об'єкта Robot
serialized_robot = pickle.dumps(robot)               # Серіалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)  # Десеріалізація об'єкта

print(deserialized_robot.__dict__) # {'name': 'Robo1', 'battery_life': 100, 'is_active': False}

#------------------------------------

class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Example("Gupalo Vasyl", 30)
print(obj.__dict__) # {'name': 'Gupalo Vasyl', 'age': 30}

obj.__dict__['city'] = 'Poltava'  # Додавання нового атрибута
print(obj.city)  # Poltava

del obj.__dict__['age']  # Видалення атрибута age
print(obj.__dict__)  # {'name': 'Gupalo Vasyl', 'city': 'Poltava'}


'''Більш практично ця техніка використовується для об'єктів, що містять несеріалізовані 
атрибути, такі як відкриті файли або з'єднання з базами даних.'''

# import pickle

# class Reader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.fh = open(self.filename, "r", encoding="utf-8")

#     def close(self):
#         self.fh.close()

#     def read(self):
#         data = self.fh.read()
#         return data

#     def __getstate__(self):
#         attributes = {**self.__dict__, "fh": None}
#         return attributes

#     def __setstate__(self, state):
#         # Відновлюємо стан об'єкта
#         self.__dict__ = state
#         self.fh = open(state["filename"], "r", encoding="utf-8")

# if __name__ == "__main__":
#     reader = Reader("data.txt")
#     data = reader.read()
#     print(data)
#     reader.close()

#     # Приклад серіалізації об'єкта Reader
#     with open("reader.pkl", "wb") as f:
#         pickle.dump(reader, f)

#     # Приклад десеріалізації об'єкта Reader
#     with open("reader.pkl", "rb") as f:
#         loaded_reader = pickle.load(f)
#         print(loaded_reader.read())
#         loaded_reader.close()


'''Створення копій об'єктів у Python може виявитися нетривіальним завданням, 
залежно від того, чи потрібна вам поверхнева (shallow) або глибока (deep) копія, 
а також від складності структури даних об'єкта.
Python намагається заощаджувати пам'ять і не копіювати дані з однієї області пам'яті 
в іншу. Натомість інтерпретатор створює нове посилання, це ще один псевдонім, на 
реальний об'єкт, замість копіювання вмісту. Така поведінка може бути небажаною'''

my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list) # [1, 2, 3, 4]


my_list = [1, 2, 3]

def square_list(x: list):
    for i, el in enumerate(x):
        x[i] = el**2
    return x
new_list = square_list(my_list)
print(new_list) # [1, 4, 9]
print(my_list) # [1, 4, 9]

#створити копію списку перед його зміною або змінити функцію, щоб вона повертала новий 
# список з квадратами елементів, замість зміни вхідного списку
def square_list(x: list):
    return [el**2 for el in x]
new_list = square_list(my_list)
print(new_list) # [1, 16, 81]
print(my_list) # [1, 4, 9]


#Для списків та словників можна скористатися явним копіюванням (через зріз для списків 
# або розпакування для словників отримати новий, незалежний об'єкт)
my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list) # [1, 2, 3] [1, 2, 3, 4]

my_dict = {1: "a"}
copy_dict = {**my_dict} # синтаксис розпакування словника **, щоб створити новий словник, 
                        # який є копією my_dict
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict) # {1: 'a'} {1: 'a', 'new_key': 'new_value'}


'''Щоб створити "поверхневу" копію об'єкта, у пакеті copy є функція copy. Ця функція 
створює новий об'єкт такого самого типу і потім створює посилання на увесь вміст 
старого об'єкта в новий. '''

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl'}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl'}, 4]

'''Поверхнева копія означає, що новий список copy_list буде містити нові посилання на 
ті ж самі об'єкти, що і оригінальний список і для об'єктів із глибокою вкладеністю така 
функція все ж таки не дасть потрібного ефекту. Тому вкладені об'єкти, такі як словник в 
третьому елементі списку, будуть спільними між оригінальним та скопійованим списками.'''

copy_list[2]["age"] = 30
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}, 4]



'''Глибока копія створює новий об'єкт та рекурсивно копіює всі вкладені об'єкти. 
В результаті, ви отримуєте повністю незалежну копію оригінального об'єкта.

Для створення глибокої копії використовуйте метод deepcopy() модуля copy. 
Ця функція рекурсивно створює нові об'єкти.'''

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl'}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]



'''Щоб створити об'єкт, який буде коректно оброблятися функціями copy та deepcopy, 
заданий клас повинен реалізувати два магічних методи: __copy__ та __deepcopy__ для 
поверхневого та глибокого копіювання відповідно.'''

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))

obj = MyClass(5)

obj_copy = copy.copy(obj) # Поверхневе копіювання
obj_copy.value = 10

obj_deepcopy = copy.deepcopy(obj) # Глибоке копіювання
obj_deepcopy.value = 20

print(obj.value, obj_copy.value, obj_deepcopy.value)
'''Викликано __copy__
Викликано __deepcopy__
5 10 20'''



'''__deepcopy__ використовує словник memo
Коли __deepcopy__ викликається для об'єкта, він перевіряє, чи існує вже копія цього 
об'єкта в словнику memo. Якщо так, метод повертає посилання на вже скопійований об'єкт 
замість створення нової копії. Це запобігає створенню кількох копій одного і того ж 
об'єкта під час глибокого копіювання та уникненню нескінченної рекурсії.

У словнику memo ключами є ідентифікатори id об'єктів, а значеннями є вже скопійовані 
об'єкти. Це дозволяє швидко перевірити, чи був об'єкт уже оброблений під час поточної 
операції копіювання.'''

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Викликано __copy__ для ComplexObject")
        # Поверхневе копіювання не копіює вкладені об'єкти глибоко
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__ для ComplexObject")
        # Глибоке копіювання копіює вкладені об'єкти
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}") # Copy object: Hello
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}") # Deepcopy object: Привіт



#--------------------------------------------

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

nested_obj.greeting = "Hello"

print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")

#-----------------------------------------

'''Уявімо, що ми працюємо з класом, який представляє налаштування користувача, і ці 
налаштування включають в себе великий набір даних (гігабайти даних), який не потрібно 
дублювати при кожному копіюванні, але з яким потрібно працювати в ізольованому середовищі.'''

import copy

class UserSettings:
    def __init__(self, preferences, large_data_reference):
        self.preferences = preferences
        self.large_data_reference = large_data_reference

    def __deepcopy__(self, memo):
        print("Кастомізоване глибоке копіювання для UserSettings")
# Припустимо, що preferences - це невеликий словник, який можна безпечно скопіювати,
# а large_data_reference - це посилання на великий об'єкт даних, яке ми не хочемо дублювати.
        new_preferences = copy.deepcopy(self.preferences, memo)
        # Передаємо посилання на ті ж великі дані замість їх копіювання
        new_obj = UserSettings(new_preferences, self.large_data_reference)
        return new_obj

# Створення екземпляра UserSettings
original_settings = UserSettings({"language": "uk"}, large_data_reference="LargeDataID")

# Глибоке копіювання з кастомізованою логікою
settings_copy = copy.deepcopy(original_settings)


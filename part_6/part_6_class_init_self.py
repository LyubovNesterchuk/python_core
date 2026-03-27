'''Спосіб організації програм, коли об'єднують дані та функціонал усередині якогось об'єкта, 
називають об'єктноорієнтованою парадигмою програмування.

Клас - це шаблон, з якого створюються об'єкти.'''

class User:
    name = 'Anonymous'
    age = 15

user1 = User()
print(user1.name) # Anonymous
print(user1.age) # 15

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name) # John
print(user2.age) # 90


'''Атрибут класу – це змінна, яка визначена на рівні класу, а не екземпляра класу. Це означає, що вона 
спільна для всіх екземплярів цього класу. Атрибути класу використовуються для зберігання даних, 
які повинні бути однаковими для всіх об'єктів класу.'''

class MyClass:
    class_attribute = "I am a class attribute" 


'''Поле класу ("атрибут екземпляра") – це змінна, яка визначена на рівні окремого екземпляра класу.
Кожен екземпляр класу має свій власний набір полів, які можуть приймати різні значення для різних 
екземплярів. Полем може бути будь-який об'єкт Python. Зазвичай це змінна, або контейнер (словник, список, 
рядок тощо). Поля класу використовуються для зберігання даних, що специфічні для кожного окремого об'єкта.

Атрибути класу визначаються за межами будь-яких методів і є спільними для всіх екземплярів класу.

Метод __init__ використовується як конструктор для ініціалізації нових об'єктів класу.

self використовується для доступу до атрибутів і методів конкретного екземпляра класу.

Методи можуть звертатися до атрибутів екземпляра через self.
Методи оголошуються всередині класу та викликаються через екземпляр класу з використанням нотації крапки.
Атрибути класу спільні для всіх екземплярів, тоді як поля унікальні для кожного.

'''


class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу
obj1 = MyClass(5)
obj2 = MyClass(10)


'''Метод класу — це функція, яка оперує з полями класу та/або аргументами, які передаються
у метод.Методи класу описують поведінку класу та як він взаємодіє з іншими об'єктами. Щоб метод 
класу міг працювати з іншими методами та полями класу, першим аргументом будь-якого методу завжди 
виступає сам об'єкт класу. Для першого аргументу можна використовувати будь-яку назву, яка не 
викликає синтаксичної помилки, однак, є домовленість завжди використовувати self.'''

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age

bob = Person('Boris', 34)

bob.say_name() # Hi! I am Boris and I am 34 years old.
bob.set_age(25) 
bob.say_name() # Hi! I am Boris and I am 25 years old.


'''Тут метод __init__() — спеціальний метод-конструктор, який автоматично виконується під час 
створення кожного нового екземпляра на базі класу Person, так ми запобігаємо конфліктам імен 
стандартних методів Python та методів наших класів.'''

'''Змінна класу або атрибут – це змінна, яка зберігається в класі та доступ до них мають усі 
екземпляри цього класу. Змінна класу існує тільки одна, та будь-який з об'єктів, коли змінює 
змінну класу, змінює її для решти екземплярів цього ж класу.
Змінна об'єкту або поле - це змінна, яка зберігається в об'єкті. Вона належать кожному окремому 
екземпляру класу. У цьому випадку кожен об'єкт має свою власну копію поля, тобто вона жодним 
чином не пов'язана з іншими такими ж полями в інших екземплярах.'''


class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")

first = Person('Boris')
first.how_many_persons() # Кількість людей зараз 1
second = Person('Alex')
first.how_many_persons() # Кількість людей зараз 1



class Person:
    count = 0

    def __init__(self):
        self.count = 10

person = Person()
print(person.count)  # 10
print(Person.count)  # 0



#--------------------------------------------------------

class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu (екземпляр pikachu класу Pokemon, ініціалізуючи його з іменем 
# "Pikachu", типом "Electric" та здоров'ям 100.
pikachu = Pokemon("Pikachu", "Electric", 100)

# метод attack може приймати інший об'єкт Pokemon як параметр
pikachu.attack(Pokemon("Charmander", "Fire", 100)) 
# Симулюємо ухилення pikachu від атаки, використовуючи метод dodge
pikachu.dodge()
# змінить значення атрибуту name об'єкта pikachu на "Raichu"
pikachu.evolve("Raichu")


'''ООП має чотири основні концепції, які відрізняють його від інших методологій програмування:
Абстракція
Інкапсуляція
Наслідування
Поліморфізм

абстракція - це модель якогось об'єкта або явища з реального світу, що відкидає незначні деталі,
які не грають істотну роль в контексті розгляду концепції ООП.
'''

'''Інкапсуляція в програмуванні, зокрема в об'єктно-орієнтованому програмуванні (ООП), 
є одним із ключових принципів, який полягає в приховуванні внутрішньої структури класу та 
захисті його даних від прямого доступу ззовні. Цей принцип дозволяє обмежити доступ до певних 
компонентів класу (полів і методів), забезпечуючи контроль над тим, як ці дані використовуються 
та змінюються.Pеалізується через використання атрибутів та методів:
публічних (public)- елемент доступний з будь-якого місця в програмі
захищених (protected) - елемент доступний з класу, в якому він оголошений, а також з класів-похідних.
приватних (private) - елемент доступний лише з класу, в якому він оголошений'''


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greeting(self) -> str:
        return f"Hi {self.name}"

p = Person("Boris", 34)


'''Захищені (Protected) атрибути та методипозначаються одним підкресленням _ на початку імені.
Правильним підходом є забезпечення доступу до захищених атрибутів через публічні методи, 
які можуть включати додаткову логіку обробки або перевірки, тим самим підтримуючи безпеку та 
цілісність даних всередині класу.'''

class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active()) # Boris 34 True
print(p.greeting()) # Hi Boris

'''Атрибути, що вважаються приватними позначаються двома підкресленнями __ і не можуть бути 
доступні безпосередньо ззовні класу.'''

class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin    

p = Person("Boris", 34, True, False)
# print(p.__is_admin) # AttributeError: 'Person' object has no attribute '__is_admin'
print(p._Person__is_admin) # False

print(p.get_is_admin()) # False
p.set_is_admin(True)
print(p.get_is_admin()) # True



'''Наслідування - це механізм ООП, який дозволяє одному класу переймати властивості та методи 
іншого класу. У Python це робиться шляхом оголошення класу, який "наслідується" від іншого класу.

Базовий або батьківський клас (superclass) це клас, від якого наслідуються властивості та методи.

Похідний або дочірній клас (subclass) це клас, який наслідує властивості та методи від базового 
класу.'''

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self) -> str:
        return "Meow"
    
class Cow(Animal):  
    def make_sound(self):
        return "Moo"
    
# Конструкція super() використовується для забезпечення того, що методи базового класу можуть 
# бути викликані з похідного класу, особливо коли ці методи перевизначаються

class Dog(Animal):
    def __init__(self, nickname: str, age: int, breed: str):
        super().__init__(nickname, age)  # Викликаємо конструктор базового класу
        self.breed = breed  # Додаємо нову властивість породу собаки
  
    def make_sound(self):
        return "Woof"

    def chase_tail(self) -> str: #  унікальний метод, який не є частиною класу Animal
        return f"{self.nickname} is chasing its tail!"

my_cat = Cat("Simon", 4)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Meow
print(my_cow.make_sound())  # Moo

my_dog = Dog("Rex", 5, "Golden Retriever")
print(my_dog.make_sound())  # Woof
print(my_dog.chase_tail())  # Rex is chasing its tail!



'''Багаторівневе наслідування - це коли клас наслідує від іншого класу, який вже є 
похідним класом. Це створює "ланцюжок" наслідування, де можливості передаються через декілька 
рівнів.
MRO (Method Resolution Order) в Python, визначає порядок, за яким класи будуть переглядатися 
під час пошуку методів. Python визначає MRO за допомогою алгоритму лінійного упорядкування.
Основна ідея цього алгоритму полягає в тому, щоб зберегти порядок визначення класів та водночас 
забезпечити, щоб базові класи були перевірені після всіх їхніх похідних класів.
'''

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound()) # Chirp
print(my_parrot.can_fly()) # True
print(my_parrot.say_phrase("Hello, World!")) # The parrot says: 'Hello, World!'

#  Виведе порядок розв'язання методів для класу (виклик відбувається на самому класі, а не екземплярі класу)
print(TalkingParrot.mro()) # [<class '__main__.TalkingParrot'>, <class '__main__.Parrot'>, <class '__main__.Bird'>, <class '__main__.Animal'>, <class 'object'>]



class A:
    name = "Я клас A"
class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"
class C(B, A):
    property = "Я знаходжусь в класі C"
c = C()
print(c.name) # Я клас B
print(c.property) # Я знаходжусь в класі C


class A:
    name = "Я клас A"
class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"
class C(A, B):
    property = "Я знаходжусь в класі C"
c = C()
print(c.name) # Я клас A
print(c.property) # Я знаходжусь в класі C



'''Поліморфізм -  дозволяє об'єктам мати різні форми або поведінку, базуючись на їх типах.
це відноситься до здатності різних класів використовувати методи з однаковою назвою, але 
з різною реалізацією. Це дозволяє використовувати один інтерфейс для різних типів даних.
'''

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)


''' (Duck Typing) качина типізація означає, що замість перевірки типу об'єкта перед його використанням, 
важливіше зосередитися на тому, чи має об'єкт потрібні методи чи властивості, які вимагаються 
для виконання певної функції або операції. "Якщо це ходить як качка і крякає як качка, то це, 
ймовірно, качка".'''

class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck) # Quack, quack!
make_it_quack(person) # I'm Quacking Like a Duck!


'''У Python можна використовувати статичну типізацію для анотації типів і одночасно 
покладатися на качину типізацію для поліморфізму та гнучкої поведінки об'єктів.
Таким чином, статична типізація допомагає забезпечити правильність типів на етапі розробки, 
а качина типізація забезпечує гнучкість у виконанні, дозволяючи об'єктам різних класів 
використовувати спільний інтерфейс.'''

# визначає набір методів, які цей параметр має виконувати, не прив'язуючись до конкретного класу.
from typing import Protocol 

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Woof
make_it_speak(cat)  # Meow
make_it_speak(robot)  # Beep boop


#---------------------------------------

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def info(self) -> dict:
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        super().__init__(nickname, weight)
        self.breed = breed
        self.owner = owner

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return self.owner.info()


# створюємо Owner
owner = Owner("Boris", 30, "Kyiv")
# передаємо об'єкт Owner
dog = Dog("Barbos", 23, "labrador", owner)

print(dog.who_is_owner()) #{'name': 'Boris', 'age': 30, 'address': 'Kyiv'}



#-----------------------------------------------------------------

'''Існує два типи полів: змінні класи та змінні об'єкта. 
вони відрізняються тим, що належать або класу чи об'єкту відповідно.

Змінні класу – доступ до них мають усі екземпляри цього класу. 
Змінна класу існує тільки одна, та будь-який з об'єктів, коли змінює змінну класу, 
змінює її для решти екземплярів цього ж класу.

Змінні об'єкта - належать кожному окремому екземпляру класу. 
У цьому випадку кожен об'єкт має свою власну копію поля, тобто вона жодним чином 
не пов'язана з іншими такими ж полями в інших екземплярах.'''


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")


first = Person('Boris')
first.how_many_persons() # Кількість людей зараз 1
second = Person('Alex')
first.how_many_persons() # Кількість людей зараз 2


#--------------------------------------------------

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = color

first_animal = Animal("h", 1)
second_animal = Animal("d", 6)

first_animal.change_color('red') 
print(first_animal)# <__main__.Animal object at 0x0000016BCDB75940>
print(first_animal.nickname) #h
'''У Python є абстракція над файлами — це вказівник на файл або файловий об'єкт.
 Файловий об'єкт — це системний ресурс, доступ до якого надає операційна система.
 можна відкрити (отримати/створити), закрити (повідомити системі, що робота з ним 
 завершена), можна записати у нього щось і прочитати щось.'''


'''вбудована функція open, в яку потрібно обов'язково передати ім'я файлу, 
який ми хочемо відкрити, і  як саме ми хочемо відкрити файл
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file - шлях до файлу у вигляді рядка (повний шлях або шлях відносно поточного каталогу виконання)
mode (необов'язковий) - режим, в якому буде відкрито файл. 
Ось основні режими які ми будемо використовувати:
'r' - читання (за замовчуванням). Файл має існувати.
'w' - запис. Створює новий файл або перезаписує той, що вже існує.
'a' - додавання. Дописує в кінець файлу, не перезаписуючи його.
'b' - бінарний режим (може бути використаний разом з іншими, наприклад 'rb' або 'wb').
'+' - оновлення (читання та запис)
'r+' дозволяє читати та додавати новий контент
'w+' видаляє вміст файлу
'x' відкриває лише нові файли.
'''

# fh = open('test_file.txt') #fh — це файловий об'єкт, через який ми можемо працювати з файлом.
'''Якщо файлу з ім'ям test_file.txt в системі немає, то ви отримаєте виняток.'''
# fh.close() # Закривати файл обов'язково. 

fh = open('test.txt', 'w') #створили (або перезаписали, якщо він вже існував) файл test.txt
symbols_written = fh.write('hello!')
print(symbols_written) # 6  метод write повертає кількість записаних у файл символів
fh.close()


fh = open('test.txt', 'w+') #відкрили файл в режимі для читання та запису, але сам файл ми перезаписуємо, якщо він існує
fh.write('Hello!')
fh.seek(0) # повернути вказівник на початок файлу 
first_two_symbols = fh.read(2)
print(first_two_symbols)  # 'He'
fh.close()

'''Метод read() читає весь вміст файлу як один рядок, 
тоді як readlines() повертає список рядків, 
а readline() читає один рядок за раз.'''

fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
all_file = fh.read()
print(all_file)  # 'hello!'
fh.close()

# Доки файловий дескриптор не закритий, ви можете читати із нього частинами, 
# продовжуючи читання з того самого місця, на якому зупинилися
fh = open('test.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol, end = '  ') # h  e  l  l  o  !
fh.close()



fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

# метод readline читати файл порядково, по одному рядку за раз
fh = open('test.txt', 'r')
while True:
    line = fh.readline() 
    if not line:
        break
    print(line)
fh.close()

# метод readlines, який читає увесь файл повністю, але повертає список рядків, 
# де елемент списку — це один рядок з файлу
fh = open('test.txt', 'r')
lines = fh.readlines()
print(lines) # ['first line\n', 'second line\n', 'third line']
fh.close()

# всі методи, які читають файли порядково, залишають (не видаляють)
# символ перенесення рядка \n. Його, за необхідності, треба видаляти самостійно
fh = open("test.txt", "r")
lines = [el.strip() for el in fh.readlines()]
print(lines) # ['first line', 'second line', 'third line']
fh.close()


# метод seek дає можливість управляти положенням курсора (вказівника) у файлі 
# та довільно переміщатися файлом 
# приймає один аргумент — це кількість символів, на які потрібно змістити курсор у файлі
# Переміщаючи курсор, можна перезаписувати символи файлу або читати записане.
fh = open('test.txt', 'w+')
fh.write('hello!') # після запису у файл курсор буде зупинений на останньому символі
fh.seek(1)
second = fh.read(1)
print(second)  # 'e'
fh.close()

# методом tell він повертає позицію (номер) символу з початку файлу, 
# де зараз знаходиться курсор.
fh = open("test.txt", "w+")
fh.write("hello!")

position = fh.tell()
print(position)  # 6

fh.seek(1)
position = fh.tell()
print(position)  # 1

fh.read(2)
position = fh.tell()
print(position)  # 3
fh.close()

'''Застосунок може виконати багато операцій між відкриттям та закриттям файлу.
В будь-якому місці може статися помилка та застосунок завершиться аварійно,
не повернувши файловий дескриптор системі, що може призводити до втрати даних.'''

fh = open('text.txt', 'w')
try:
    # Виконання операцій з файлом
    fh.write('Some data')
finally:
    # Закриття файлу в блоці finally гарантує, що файл закриється навіть у разі помилки
    fh.close()



'''Для покращення читабельності коду при збереженні функціоналу можна скористатися
менеджером контексту with. 
Менеджер контексту в Python - це спосіб використання ресурсів, який автоматично забезпечує 
правильне закриття файлу, незалежно від того, чи виникла помилка чи ні. 
Це робить код не тільки більш читабельним, але й безпечнішим.'''

with open('text.txt', 'w') as fh:
    # Виконання операцій з файлом
    fh.write('Some data')
# Файл автоматично закриється після виходу з блоку with

with open("test.txt", "w") as fh:
    fh.write("first line\nsecond line\nthird line")

with open("test.txt", "r") as fh:
    lines = [el.strip() for el in fh.readlines()]

print(lines) # ['first line', 'second line', 'third line']


'''роботу з текстовими фалами в кодуванні UTF-8. 
Це режим роботи з файлами за замовчуванням. Якщо ж потрібно працювати не з текстовими файлами,
то можна вказати режим відкриття файлів як b, скорочено від bytes. 
У такому режимі ви отримаєте файловий об'єкт для роботи з файлом в режимі байт-рядків.'''

with open('raw_data.bin', 'wb') as fh: #відкрили файл у режимі для запису "сирих" даних
    fh.write(b'Hello world!')


'''у Python є вбудовані типи даних байт-рядків
bytes - незмінний тип, що використовують для представлення байтів.
bytearray - змінний тип, що дозволяє модифікувати байти після їх створення.'''

'''Біт є основною одиницею інформації в обчислювальній техніці та цифровій комунікації.
Біт може мати одне з двох значень: 0 або 1.
 
Байт - це послідовність з 8 бітів, яка є стандартною одиницею вимірювання кількості інформації
в комп'ютерах. Один байт може представляти 256 різних станів. Від 00000000 до 11111111 
у двійковому форматі або від 0 до 255 в десятеричному
у кодуванні ASCII символ 'A' представляється як 01000001.

Усі дані на комп'ютері зберігаються у вигляді байтів. 
текстовий файл розміром у 1 кілобайт займає 1024 байти в пам'яті комп'ютера. 
Коли дані передаються через інтернет мережу, вони також розбиваються на байти.

Для байт-рядків застосовуються ті самі обмеження і правила, що і для звичайних рядків. 
Наприклад, ви можете використовувати методи upper(), startswith(), index(), find() і так далі.
'''
s = b'Hello!'# байт-рядок
print(s[1])  # Виведе: 101 (це ASCII-код символу 'e')

'''ASCII (American Standard Code for Information Interchange -
Американський стандартний код для обміну інформацією) - це символьна кодова таблиця,
яка використовується для представлення тексту в комп'ютерах, комунікаційному обладнанні 
та інших пристроях, що працюють з текстом. Кожен символ у таблиці ASCII відповідає певному числу.

ASCII визначає 128 символів, що включають латинські літери, цифри, знаки пунктуації,
а також символи управління. Кожен символ кодується 7-бітним числом (від 0 до 127)
розширений ASCII, який використовує 8-бітне кодування для представлення 256 символів 
(від 0 до 255).

приклади ASCII-кодів
Цифри: '0' - 48, '1' - 49, ..., '9' - 57.
Великі латинські літери: 'A' - 65, 'B' - 66, ..., 'Z' - 90.
Малі латинські літери: 'a' - 97, 'b' - 98, ..., 'z' - 122.
Спеціальні символи: пробіл - 32, '!' - 33, '@' - 64 тощо.

Але ASCII не підтримує символи багатьох мов, що не використовують латинський алфавіт. 
Через це були розроблені інші формати кодування, такі як UTF-8
 '''

byte_str = 'some text'.encode() #забезпечує зв'язок  між текстом (рядками Unicode) 
# та байтами, які можуть бути використані в бінарних операціях або в передачі даних по мережі
print(byte_str)

'''.encode() перетворює рядок у байтову послідовність, дозволяє стандартизувати рядок для 
операцій, які вимагають однакового представлення символів, незалежно від системи або платформи

str.encode(encoding="utf-8", errors="strict")

encoding - вказує метод кодування. По замовчуванню використовується 'utf-8'
errors - вказує, як обробляти помилки кодування.
'strict' для викидання винятку у випадку помилки, 
'ignore' для ігнорування помилок 
'replace' для заміни неможливих для кодування символів на певний замінник (?).
'''

# Перетворення списку чисел у байт-рядок за допомогою вбудованої функції bytes
numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
# Для виведення байтів найзручніше скористатися шістнадцятковим записом, 
# в якому для запису чисел від 0 до 255 достатньо двох символів.
print(byte_numbers)  # Виведе байтове представлення чисел b'\x00\x80\xff'

# Символ \x є індикатором шістнадцяткового запису кожного байта.

'''вбудована функція hex, яка перетворить ціле число в рядок — 
представлення числа в шістнадцятковій формі'''
for num in [127, 255, 156]:
  print(hex(num), end = '  ') # 0x7f  0xff  0x9c  0x вказують на шістнадцяткову форму запису 

'''Такий механізм корисний у різноманітних сценаріях, включаючи низькорівневе програмування, 
роботу з мережевими протоколами та обробку бінарних файлів'''

'''Python за замовчуванням використовує UTF-8, в якій один символ може займати від 1 до 4 байт
, і всього в алфавіті може бути до 1 112 064 знаків. Це не єдине кодування, 
на різних платформах можуть бути присутні власні, наприклад CP-1251 
(кирилиця на ОС сімейства Windows), UTF-16, UTF-32 та інші.


Щоб дізнатися, якому елементу в UTF-8 відповідає символ, є функція ord (від order).'''
ord('a')  # 97

'''коли потрібно дізнатися, який символ закодований числом, — функція chr (від character)'''
chr(100)  # 'd'

s = "Привіт!"

utf8 = s.encode()
print(f"UTF-8: {utf8}") # UTF-8: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd1\x96\xd1\x82!'

utf16 = s.encode("utf-16")
print(f"UTF-16: {utf16}") # UTF-16: b'\xff\xfe\x1f\x04@\x048\x042\x04V\x04B\x04!\x00'

cp1251 = s.encode("cp1251")
print(f"CP-1251: {cp1251}") #CP-1251: b'\xcf\xf0\xe8\xe2\xb3\xf2!'

s_from_utf16 = utf16.decode("utf-16")
print(s_from_utf16 == s) #True

print(b'Hello world!'.decode('utf-16')) # 效汬⁯潷汲Ⅴ  якщо кодування UTF-8 ми намагаємось декодувати в UTF-16

# Відкриття текстового файлу з явними вказівками UTF-8 кодування 
# навіть якщо операційна система використовує інше кодування за замовчуванням, 
# файл буде коректно відкритий із використанням UTF-8, що гарантує правильне відображення тексту
with open('text.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content) # Some data



byte_array = bytearray(b'Kill Bill')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array) # bytearray(b'Bill Kill')

'''відмінність масива байтів від байт-рядків — це змінність, щоб змінити масив байтів, 
не потрібно створювати новий. Друга важлива відмінність — це те, що масив байтів сприймається 
системою як послідовність чисел від 0 до 255, а не як послідовність символів в ASCII кодуванні. 
дозволяє додавати та видаляти елементи'''

byte_array = bytearray(b"Hello")
byte_array.append(ord("!"))  
print(byte_array) # bytearray(b'Hello!')


#bytearray  можна легко перетворити в рядок  за допомогою методу decode(), 
# вказавши потрібне кодування.
byte_array = bytearray(b"Hello World")
string = byte_array.decode("utf-8")
print(string)  # Виведе: 'Hello World'

'''bytearray корисний при обробці бінарних даних (при читанні файлів у бінарному режимі, 
обробці мережевих пакетів, або при роботі з образами даних у пам'яті)'''


string1 = "Hello World"
string2 = "hello world"
if string1.lower() == string2.lower():
    print("Рядки однакові")
else:
    print("Рядки різні")

'''метод casefold() є більш радикальним: він призначений для видалення усіх відмінностей 
у регістрі, які можуть виникати в різних мовах'''

text = "Python Programming"
print(text.casefold()) # python programming

# головне застосування casefold() для мов, де одна літера може мати різні верхній 
# та нижній регістри, наприклад, в німецькій мові.
german_word = 'straße'  # В нижньому регістрі
search_word = 'STRASSE'  # В верхньому регістрі

# Порівняння за допомогою lower()
lower_comparison = german_word.lower() == search_word.lower()

# Порівняння за допомогою casefold()
casefold_comparison = german_word.casefold() == search_word.casefold()

print(f"Порівняння з lower(): {lower_comparison}") # Порівняння з lower(): False
print(f"Порівняння з casefold(): {casefold_comparison}") # Порівняння з casefold(): True




'''Пакет shutil підтримує архіви zip, tar, gz (пакети zipfile та tarfile)

Функція shutil.make_archive() в Python використовується для створення архівів
з заданої директорії

shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
base_dir - директорія всередині архіву, з якої почнеться архівація.
'''

import shutil
# Створення ZIP-архіву з вмістом директорії 'my_folder'
shutil.make_archive('example', 'zip', root_dir='my_folder')

# Створення TAR.GZ-архіву
shutil.make_archive('example', 'gztar', root_dir='my_folder')

'''Функція shutil.unpack_archive() використовується для розпакування архівних файлів

shutil.unpack_archive(filename, extract_dir=None, format=None)

filename - шлях до архівного файлу, який потрібно розпакувати.
extract_dir - директорія, куди буде розпаковано вміст архіву. 
Якщо не вказано, використовується поточна директорія.
format - формат архіву наприклад, zip, tar, gztar, bztar, або xztar. 
Якщо параметр не вказано, Python намагається визначити формат автоматично.
'''

# Розпакування ZIP-архіву в певну директорію
shutil.unpack_archive('example.zip', 'destination_folder')

'''shutil.copy(src, dst) копіює файл з src в dst. Якщо dst є директорією, файл буде 
скопійований зі своїм поточним іменем у цю директорію.
shutil.copytree(src, dst) рекурсивно копіює всю директорію src в директорію dst.
shutil.move(src, dst) переміщує файл або директорію src в dst.
shutil.rmtree(path) рекурсивно видаляє директорію path.
shutil.disk_usage(path) повертає статистику використання диска, що містить загальний об'єм, 
використаний об'єм і вільний об'єм для даного шляху.'''

# Копіюємо файл
source_file = '/path/to/source/file.txt'
destination_dir = '/path/to/destination'
shutil.copy(source_file, destination_dir)

# Копіюємо всю директорію
source_dir = '/path/to/source/directory'
destination_dir = '/path/to/destination/directory'
shutil.copytree(source_dir, destination_dir)



'''pathlib - це модуль у Python, який надає класи для обробки файлових шляхів 
у об'єктно-орієнтованому стилі

PurePath дозволяє виконувати такі операції, як розділення шляху на частини, перевірка суфіксів, імен файлів, шляхів тощо.
методи:
p.parent вказує на батьківську директорію;
p.name повертає лише рядок з ім'ям директорі або файлу, на який вказує p;
p.suffix повертає рядком розширення файлу, на який вказує p, починаючи з крапки;

Path варто сприймати як вказівку на файл або директорію. 

'''

from pathlib import PurePath

p = PurePath("/usr/bin/simple.jpg")
print("Name:", p.name)  # Name: simple.jpg
print("Suffix:", p.suffix) # Suffix: .jpg
print("Parent:", p.parent) # Parent: \usr\bin

# Код демонструє  інтеракцію з файловою системою через об'єктно-орієнтований інтерфейс pathlib:
from pathlib import Path
# створюється об'єкт Path, який вказує на файл example.txt у директорії де був запущений скрипт
p = Path("example.txt") 
# За допомогою методу write_text(), у цей файл записується рядок "Hello, world!".
p.write_text("Hello, world!") 
# за допомогою методу read_text() вміст файлу читається і виводиться на екран.
print(p.read_text()) # Hello, world!
#  метод exists() використовується для перевірки існування файлу, результат чого також виводиться на екран.
print("Exists:", p.exists()) # Exists: True


'''Клас Path автоматично адаптується до особливостей шляхів у різних операційних системах.
Наприклад, у Windows використовуються зворотні слеші (\), тоді як в Unix-подібних системах 
(Linux, macOS) - прямі слеші (/).'''

# Для Unix/Linux
path_unix = Path("/usr/bin/python3")
# Для Windows
path_windows = Path("C:/Users/Username/Documents/file.txt")

# Початковий шлях
base_path = Path("/usr/bin")
# Додавання додаткових частин до шляху
full_path = base_path / "subdir" / "script.py"
print(full_path)  # Виведе: /usr/bin/subdir/script.py

'''Абсолютний шлях - це повний шлях до файлу або директорії від кореня файлової системи. 
Він містить всю інформацію, необхідну для знаходження файлу або директорії.
Приклад на Unix/Linux: /home/user/documents/example.txt
Приклад на Windows: C:\Users\user\documents\example.txt
Абсолютні шляхи використовують, коли потрібно точно вказати місцезнаходження файлу 
або директорії, незалежно від поточного робочого каталогу програми

Відносний шлях - це шлях до файлу або директорії відносно поточного робочого каталогу.
Він не містить повну інформацію про місцезнаходження і залежить від місця, з якого виконується
програма.'''

from pathlib import Path

# Перетворення відносного шляху в абсолютний
relative_path = Path("documents/example.txt") # створює відносний шлях.
# Метод absolute() перетворює його в абсолютний шлях, виходячи з поточного робочого каталогу.
absolute_path = relative_path.absolute()
print(absolute_path)

# Перетворення відносного шляху в абсолютний
current_working_directory = Path("E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
# метод relative_to() використовується для отримання відносного шляху щодо заданої директорії.
relative_path = absolute_path.relative_to(current_working_directory)
print(relative_path)



# Початковий шлях до файлу
original_path = Path("documents/example.txt")

# Метод with_name замінює ім'я файлу в шляху на нове, 
# коли вам потрібно зберегти решту шляху незмінною.
new_path = original_path.with_name("report.txt")
print(new_path) # documents\report.txt


# Метод with_suffix замінює або додає розширення файлу в шляху, 
# коли потрібно змінити тип файлу або додати розширення до файлу, який його не має.
original_path = Path("documents/example.txt")
new_path = original_path.with_suffix(".md") # додає розширення .md до шляху
print(new_path) #documents\example.md

'''методи with_name і with_suffix в класі Path модуля pathlib в Python 
не змінюють фізичне ім'я файлу на диску. Замість цього, вони використовуються для створення 
нового об'єкта Path, який відображає змінений шлях.'''

original_path = Path("documents/example.txt")
# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
print(original_path) # documents\example.txt
print(new_path) # documents\report.txt

'''Щоб фізично змінити ім'я файлу на диску, потрібно використовувати методи для роботи 
з файловою системою, наприклад, rename. Цей виклик змінить ім'я файлу example.txt 
на report.txt у директорії documents на диску.'''

# Створює новий об'єкт Path з іншим ім'ям файлу
new_path = original_path.with_name("report.txt")
original_path.rename(new_path)

'''Методи read_text() та write_text() використовуються для читання та запису текстових файлів.
Path.read_text(encoding=None, errors=None)
Path.write_text(data, encoding=None, errors=None)
'''
# Створення об'єкту Path для файлу
file_path = Path("example.txt")
# Запис тексту у файл
file_path.write_text("Привіт світ!", encoding="utf-8")
# Читання тексту з файлу
text = file_path.read_text(encoding="utf-8")
print(text) # Привіт світ!

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")
# Бінарні дані для запису
data = b"Python is great!"
# Запис байтів у файл
file_path.write_bytes(data)

# Створення об'єкту Path для бінарного файлу
file_path = Path("example.bin")
# Читання байтів з файлу
binary_data = file_path.read_bytes()
print(binary_data) # b'Python is great!'


'''Метод iterdir() використовується для отримання переліку всіх файлів та піддиректорій у
 вказаній директорії. Цей метод повертає ітератор, який виробляє об'єкти Path для кожного 
 файлу та піддиректорії у директорії, що визначена поточним об'єктом Path.'''

# Створення об'єкту Path для директорії
directory = Path("./picture")
# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)
'''
picture\bot-icon.png
picture\Logo
picture\mongodb.jpg

📦core_course
 ┣ 📂picture
 ┃ ┣ 📂Logo
 ┃ ┣ 📜bot-icon.png
 ┃ ┗ 📜mongodb.jpg
 ┗ 📜ex01.py
'''

'''Для створення нової директорії використовується метод mkdir().

Path.mkdir(mode=0o777, parents=False, exist_ok=False)
mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.
'''
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)

'''Для видалення директорії використовується метод rmdir(). Він видаляє директорію, 
але директорія повинна бути порожньою.'''

directory = Path('/my_directory/new_folder')
directory.rmdir()

'''метод exists() перевіряє, чи існує файл або директорія.
метод is_dir() перевіряє, чи є об'єкт директорією.
метод is_file() перевіряє, чи є об'єкт файлом.'''

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує") # picture існує

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією") # picture є директорією

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")

'''Функція shutil.copy() копіює вміст файлу, 
але не копіює метадані, тоді як shutil.copy2() копіює і вміст, і метадані.'''

# Вихідний і цільовий файли
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')
# Копіювання файла
shutil.copy(source, destination)

'''Для переміщення файлів використовується функція shutil.move().'''
# Вихідний і цільовий шляхи
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')
# Переміщення файла
shutil.move(source, destination)

'''Метод stat() повертає інформацію про файл, включаючи його розмір атрибут st_size
надає час створення, атрибут st_ctime , 
і час останньої модифікації файлу, атрибут st_mtime.'''

file_path = Path("./picture/bot-icon.png")
# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів") # Розмір файла: 2876 байтів


from pathlib import Path
import time

file_path = Path("./picture/bot-icon.png")
# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}") # Час створення: Fri Dec 29 04:43:16 2023
print(f"Час модифікації: {time.ctime(modification_time)}") # Час модифікації: Thu May 17 19:59:44 2018


'''. Для видалення файлу використовується метод unlink(). 
Він видаляє файл, на який вказує об'єкт Path.

Path.unlink(missing_ok=False)
Параметр missing_ok якщо має значення True, то виняток не буде викинуто, якщо файл не існує.
За замовчуванням False, це означає, що буде викинуто виняток FileNotFoundError, 
якщо файл не існує.
'''
# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')
# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists(): # перевіряємо, чи він існує, щоб уникнути винятку FileNotFoundError
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')
# або
file_path.unlink(missing_ok=True)






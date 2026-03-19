from sys import argv
from pathlib import Path
from itertools import zip_longest


if len(argv) !=3:
    print("Please provide file paths for two files")
    exit()

# item_first_path=argv[1]
# item_second_path=argv[2]

#item_first_path, item_second_path= argv[1], argv[2]

item_first_path, item_second_path = argv[1:]

print(item_first_path)
print(item_second_path)

item_first = Path(item_first_path)
item_second = Path(item_second_path)

if item_first.is_dir() and item_second.is_dir():
    print(f"Both {item_first} {item_second}are folders")
    exit() 
if item_first.is_dir():
    print(f"{item_first} is a folder")
    exit()
if item_second.is_dir():
    print(f"{item_second} is a folder")
    exit() 


with open(item_first) as file_first:
    file_first_lines = file_first.readlines()
    print(file_first_lines)
with open(item_second) as file_second:
    file_second_lines = file_second.readlines()
    print(file_second_lines)

# for i in range(len(file_first_lines)):
#     if file_first_lines[i] != file_second_lines[i]:
#         print(i + 1)
#         print(f"> {file_first_lines[i].rstrip()}")
#         print(f"< {file_second_lines[i].rstrip()}")

for i, (file_first_line, file_second_line) in enumerate(zip_longest(file_first_lines, file_second_lines, fillvalue = "")):
    if file_first_line != file_second_line: # різна кількість рядків у файлах тому використовуємо не zip, а zip_longest
        print(i + 1)
        print(f"> {file_first_line.rstrip()}")
        print(f"< {file_second_line.rstrip()}")

# в терміналі ввести 
# python diff.py test1.txt joke
# python diff.py test1.txt test2.txt
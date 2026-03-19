from sys import argv
from pathlib import Path

#item_path = "." if len(argv) !=2 else argv[1] #тернарний рядок

if len(argv) !=2:
    print("Please provide a file path")
    exit()

item_path=argv[1]
item = Path(item_path)

if item.is_dir():
    print(f"{item} is a folder")
    exit()

with open(item_path) as file:
    #for line in file.readlines():
    for line in file:
        print(line)

# запустити в терміналі: 
# python cat.py
# python cat.py test1.txt
# python cat.py joke
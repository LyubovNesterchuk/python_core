from sys import argv
from colorama import Fore, Style
from pathlib import Path

folder_path = "." if len(argv) !=2 else argv[1] #тернарний рядок
# if len(argv) !=2:
#     print("No path provided")
#     folder_path="."
# else:
#     folder_path=argv[1]
p = Path(folder_path)

for folder_item in p.iterdir():
    if folder_item.is_dir():
        print(Fore.BLUE + str(folder_item) + "/"+ Style.RESET_ALL)
    else:
        print(folder_item)


print(p) # запустити в терміналі python ls.py .
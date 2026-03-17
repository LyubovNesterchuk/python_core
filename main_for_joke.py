'''задача написати скрипт, який:
Під час запуску запитує в користувача ім'я;
Вітається з користувачем на ім'я;
Запитує чи не бажає користувач прочитати анекдот;
Якщо користувач відповідає "так", то видає випадковий рядок із файлу "jokes.txt" і повторює пункти 3 та 4;
Якщо відповідь "ні", то прощається на ім'я і завершує роботу.

Для створення такої програми, ми можемо організувати все наступним чином. 
Основний скрипт main.py буде відповідати за взаємодію з користувачем: запитування імені, 
вітання, запит на читання анекдоту та завершення роботи. Для формування самих жартів
ми створимо пакет "joke". Цей пакет буде містити функціонал для вибору випадкового анекдоту 
з файлу "jokes.txt".

Отже структура нашого проєкту буде наступною
📦pythone_core
 ┣ 📂joke
 ┃ ┣ 📜jokes.txt
 ┃ ┣ 📜jokes_handler.py
 ┃ ┗ 📜__init__.py
 ┗ 📜main_4.py'''

from pathlib import Path
from joke import get_random_joke


parent_folder_path =Path(".")
def parse_folder(path):
    for element in path.iterdir():
        if element.is_dir():
            print(f"Parse folder: This is folder - {element.name}")
        if element.is_file():
            print(f"Parse folder: This is file - {element.name}")
parse_folder(parent_folder_path)

# folder = Path("joke")
# folder.mkdir(exist_ok=True)
# (folder / "jokes.txt").touch() #.touch() → створює файл
# (folder / "jokes_handler.py").touch()
# (folder / "__init__.py").touch()

'''краще створити в терміналі:
mkdir joke
touch joke/__init__.py
touch joke/jokes_handler.py
touch joke/jokes.txt'''


file_path = "joke/jokes.txt"
data = ['Чому програмісти не люблять природу? Тому що в ній забагато помилок.',
'Двоє томатів переходили дорогу. Один каже іншому: "Швидше, інакше ми перетворимося на кетчуп!"',
'Яка різниця між кавою та вашим думками? Кава завжди працює.',
'Чому електрони ніколи не вірять в атоми? Бо в атомах забагато позитиву.',
'Учитель математики запитує учня: "Якщо у мене є п\'ять яблук в одній руці і шість яблук в іншій, що це дасть? Учень: "Великі руки".'
]

with open(file_path, "w", encoding="utf-8") as file:
    file.write("\n".join(data))


def main():
    name = input("Будь ласка, введіть ваше ім'я: ")
    print(f"Привіт, {name}!")

    while True:
        user_response = input(f"{name}, бажаєте почути анекдот? (так/ні): ").lower()
        if user_response == "так":
            print(get_random_joke())
        elif user_response == "ні":
            print(f"До побачення, {name}!")
            break

if __name__ == "__main__":
    main()

'''Конструкція if __name__ == "__main__": перевіряє, чи запускається файл безпосередньо, 
а не імпортується як модуль, і тільки в цьому випадку викликає main().'''
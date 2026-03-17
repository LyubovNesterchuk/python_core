import random
import pathlib

# мінна current_dir визначає директорію, де знаходиться файл скрипту.
#  Нам це необхідно, щоб шлях до файлу current_dir / "jokes.txt" завжди був вірний
# де б ми не виконали нашу програму.
current_dir = pathlib.Path(__file__).parent 

def get_random_joke():
    try:
        with open(current_dir / "jokes.txt", "r", encoding="utf-8") as file:
            jokes = file.readlines()
            return random.choice(jokes).strip()
    except FileNotFoundError:
        return "Не вдалося знайти файл з анекдотами."

'''файл jokes.txt відкривається за допомогою контекстного менеджера with, 
що гарантує правильне закриття файлу після завершення роботи з ним.'''
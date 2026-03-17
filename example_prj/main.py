'''📦example_prj
 ┣ 📜data.py
 ┣ 📜main.py
 ┣ 📜processing.py
 ┗ 📜temperatures.txt'''
from pathlib import Path
from data import load_data, clean_data
from processing import calculate_statistics

def main():
    # Для проєктів з кількома файлами завжди краще використовувати Path(__file__).parent, 
    # щоб файли даних шукалися відносно скрипта. Так твій код стає незалежним від того, 
    # де запускаєш Python
    BASE_DIR = Path(__file__).parent # Отримуємо директорію, де лежить main.py
    filename = BASE_DIR / "temperatures.txt"
    
    raw_data = load_data(filename)
    temperatures = clean_data(raw_data)
    stats = calculate_statistics(temperatures)

    if stats:
        print(f"Minimum Temperature: {stats['min']}°C")
        print(f"Maximum Temperature: {stats['max']}°C")
        print(f"Average Temperature: {stats['average']:.2f}°C")
        print(f"Median Temperature: {stats['median']:.2f}°C")
    else:
        print("No temperature data available.")

if __name__ == "__main__":
    main()


'''Minimum Temperature: 21.8°C
Maximum Temperature: 26.3°C
Average Temperature: 24.38°C
Median Temperature: 24.45°C
'''
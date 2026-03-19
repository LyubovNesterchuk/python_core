
# читає дані з файлу та повертає список рядків
def load_data(filename: str) -> list[str]: 
    with open(filename, "r") as file:
        return file.readlines()
    

# виконує очищення даних та перетворює рядки в числа і відкидає порожні рядки.
def clean_data(temperature_data: list[str]) -> list[float]:
    return [float(temp.strip()) for temp in temperature_data if temp.strip()]


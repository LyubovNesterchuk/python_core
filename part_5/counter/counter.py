
# from pathlib import Path
# from collections import defaultdict, Counter

# #1) прочитати рядки з файлу
# current_directory = Path(__file__).parent
# def read_lines_from_file(file_path: str) -> list[str]:
#      with open(file_path, encoding = "utf-8") as file:
#           return file.readlines()
# print(__file__)          
# print(read_lines_from_file(current_directory/"counter.txt"))

# my_str = '5, 6, 1, 3\n'.strip()
# print (my_str.split()) #['5,', '6,', '1,', '3,']

#2) з рядка дістати окремі числа

# def convert_file_line_to_numbers_list(line: str) -> list[int]:
#     numbers_list = []
#     numbers_str_list = line.strip().split(",")
#     for  numbers_str in  numbers_str_list:
#          numbers_list.append(int(numbers_str))
#     return numbers_list

# print(convert_file_line_to_numbers_list(my_str))


#3)
# def calculate_statistics(element_list: list[int]) -> dict[int, int]:
#     statistics_dict ={}
#     for element in element_list:
#         #зустрічаємо елемент вперше
#         if element not in statistics_dict:
#             statistics_dict[element] = 0
#         statistics_dict[element] += 1
#     return statistics_dict
# print(calculate_statistics(my_str))

# def calculate_statistics_default_dict(element_list: list[int]) -> dict[int, int]:
#     statistics_dict = defaultdict(int)
#     for element in element_list:
#         statistics_dict[element] += 1
#     return statistics_dict


# def calculate_statistics(element_list: list[int]) -> dict[int, int]:
#     return Counter(element_list)
# print(calculate_statistics(my_str))


###############################################################
# my_default_dict = defaultdict(int)
# print(my_default_dict)# defaultdict(<class 'int'>, {})
# my_default_dict[10] += 1 
# print(my_default_dict) # defaultdict(<class 'int'>, {10: 1})

# my_default_dict = defaultdict(list)
# print(my_default_dict)# defaultdict(<class 'list'>, {})
# my_default_dict[10].append("a")
# print(my_default_dict) # defaultdict(<class 'list'>, {10: ['a']})



'''написати функцію, яка рахуватиме кількість появи кодного числа у рядку, 
вивести у терміна число, яке зустрічається найчастіше'''
from pathlib import Path
from collections import Counter

def most_frequent_number_from_file(filename):
    current_directory = Path(__file__).parent
    # Відкриваємо файл і читаємо його вміст
    with open(current_directory / filename, 'r', encoding='utf-8') as file:
        numbers = file.read().split()  # розбиваємо текст на слова/числа

    counts = Counter(numbers)  # рахуємо кількість кожного числа
    
    # Знаходимо число з максимальною кількістю появ
    most_common_num, _ = counts.most_common(1)[0]
    
    return most_common_num.strip(",")

result = most_frequent_number_from_file("counter.txt")
print(f"Найчастіше зустрічається число: {result}")
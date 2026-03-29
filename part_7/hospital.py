''' Є лікарня, в якій є Лікарі та Пацієнти. У кожного Пацієнта є Історія_хвороб\
В Історії_хвороб зберігається 10 останніх Хвороб.\
Хвороба містить інформацію про те, коли пацієнт захворів, хто його лікував, коли одужав (якщо одужав),\
процедури та лікування, які призначив лікар.\
Лікар може призначати процедури (наприклад діагностичні) та лікування (наприклад курс ліків).
У лікарів і пацієнтів є Ім'я та Прізвище. У пацієнтів є номер поліса соціального страхування.
У лікарів є посада. Пацієнт не може змінювати свою Історію_хвороб.
Завдання: реалізувати в класах наведені вище умови.'''

from datetime import datetime
from collections import UserList, deque

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class NoRight(Exception):
    pass

class Disease:
    def __init__(self, name, doctor):
        self.name = name
        self.doctor = doctor
        self.treatment = list()
        self.time = datetime.now()
        self.cured = False
        self.cure_time = None

    def cure(self):
        self.cured = True
        self.cure_time = datetime.now()

    def treat(self, treatment):
        self.treatment.append(treatment)

class Story(UserList):
    story_size = 10

    def __init__(self):
        self.__data = deque([], self.story_size)
        self.__data__dict = dict()
        self.data = list()

    def __getitem__(self, key=None):
        if key is None:
            return list(self.__data)
        if isinstance(key, int):
            return self.__data[key]
        elif isinstance(key, str):
            return self.__data__dict.get(key)

    def __len__(self):
        return len(self.__data)

    def add(self, *_):
        raise NoRight

    def __add(self, disease):
        self.__data.append(disease)
        self.__data__dict = {des.name: des for des in self.__data}
        self.data = [des for des in self.__data]

    @property
    def healthy(self):
        return all([disease.cured for disease in self.__data])

class Patient(Person):
    def __init__(self, name, surname, polis):
        super().__init__(name, surname)
        self.polis = polis
        self.story = Story()

    @property
    def healthy(self):
        return self.story.healthy

class Doctor(Person):
    def __init__(self, name, surname, position):
        super().__init__(name, surname)
        self.position = position

    def add(self, patient, disease_name):
        des = Disease(disease_name, ' '.join((self.name, self.surname)))
        patient.story._Story__add(des)

    def treat(self, patient, disease_name, treatment):
        patient.story[disease_name].treat(treatment)



doctor_surg = Doctor('Bill', "Klinton", "Head")
doctor_tera = Doctor('Tom', 'Jerry', 'Therapist')

patient_one = Patient("George", 'Bush', 123456789)
patient_two = Patient('Barak', 'Obama', 987654321)

doctor_tera.add(patient_one, 'flu')
doctor_surg.add(patient_two, 'appendicit')

print(patient_one.story['flu'].time)
print(patient_two.story['appendicit'].time)

doctor_tera.treat(patient_one, 'flu', 'medicine')
doctor_surg.treat(patient_two, 'appendicit', 'operation')

print(patient_one.story['flu'].treatment)
print(patient_two.story['appendicit'].treatment)

print(patient_one.healthy)

patient_one.story['flu'].cure()
print(patient_one.healthy)        

'''2026-03-29 18:09:21.329589
2026-03-29 18:09:21.329589
['medicine']
['operation']
False
True'''
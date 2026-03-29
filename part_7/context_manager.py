'''Написати Contex Manager FileReader, який пише в лог timestamp, коли файл був відкритий, 
timestamp, коли файл був закритий, ім'я файлу, і як довго файл був відкритий з точністю до секунд.'''

from datetime import datetime
from time import sleep

class FileReader:

    def __init__(self, filename):
        self.file = None
        self.opened = None
        self.log = ''
        self.tmstmp = None
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.tmstmp = datetime.now().timestamp()
        msg = '{:<20}|{:^15}|\n'.format(self.tmstmp, self.filename)
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            tmstmp = datetime.now().timestamp()
            diff = tmstmp - self.tmstmp
            msg = '{:<20}|{:^15}|{:>4.0f}\n'.format(tmstmp, self.filename, diff)
            self.log += msg
        self.opened = False
        if exc_val is not None:
            print("Oh NO!!!")

reader = FileReader('new_file.txt')

with reader as f:
    print(f.read())

with reader as f:
    sleep(2)
    print(f.read())

print(reader.log)


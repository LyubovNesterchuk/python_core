''' Створити клас для збереження паролю з можливістю його зміни і додавання закритої інформації'''

class KeyStore:
    def __init__(self, name, password):
        self.__password = None
        self.__secret = None
        self.name = name
        self.password = password


    @property
    def password(self):
        return 'No way to get password back'

    @password.setter
    def password(self, value):
        if self.__password is None:
            self.__password = value
        else:
            if self.validate():
                print('Password correct')
                self.__password = value
            else:
                print('Incorrect')

    @property
    def secret(self):
        if self.validate():
            return self.__secret

    @secret.setter
    def secret(self, value):
        if self.validate():
            self.__secret = value

    def validate(self):
        value = input("Password: ")
        if self.__password == value:
            print('Ok')
            return True
        print("Wrong password")
        return False

k_store = KeyStore('Krab', '123456')
k_store.password = '111'
print(k_store.password)
k_store.password = '567890'
k_store.secret = 'TEST'
print(k_store.secret)
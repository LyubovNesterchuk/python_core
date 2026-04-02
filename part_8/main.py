import pickle

# 1--------------------------------

data = {"some_password": 1234567890}

with open ("my_dict.bin", 'wb') as file:
    pickle.dump(data, file)

with open("my_dict.bin", 'rb') as file:
    my_dict = pickle.load(file)

print(my_dict) # {'some_password': 1234567890}
data_types = pickle.dumps(data)
print(data_types) # b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\rsome_password\x94J\xd2\x02\x96Is.'
print(pickle.loads(data_types))  # {'some_password': 1234567890}



# 2 ---------------------------------------------------

FILENAME = 'users.dat'
users = [
    ['Tom', 28, True],
    ['Alice', 23, True],
    ['Oleh', 99, False]
]

with open (FILENAME, 'wb') as file:
    pickle.dump(users, file)

with open(FILENAME, 'rb') as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print(f"Name: {user[0]}\tAge: {user[1]}\tDriver License: {user[2]}")
'''Name: Tom       Age: 28 Driver License: True
Name: Alice     Age: 23 Driver License: True
Name: Oleh      Age: 99 Driver License: False'''


# 3 ----------------------------------------------------------------------------------

class Absolute:
    value = 'some data'

    def __init__(self):
        print('Hello')
        self.data = "Hi"

instance = Absolute()

serialization_instanse = pickle.dumps(instance)
serialization_absolute = pickle.dumps(Absolute)

restored_instance = pickle.loads(serialization_instanse)
restored_absolute = pickle.loads(serialization_absolute)

print(instance.value, instance.data) # some data Hi
print(restored_instance.value, restored_instance.data) # some data Hi

print(dir(restored_instance)) #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', 'data', 'value']
print(dir(restored_absolute)) #['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slotnames__', '__str__', '__subclasshook__', '__weakref__', 'value']

print(restored_instance.__dict__) # {'data': 'Hi'}
print(restored_absolute.__dict__) # {'__module__': '__main__', 'value': 'some data', '__init__': <function Absolute.__init__ at 0x0000026B9A8EAFC0>, '__dict__': <attribute '__dict__' of 'Absolute' objects>, '__weakref__': <attribute '__weakref__' of 'Absolute' objects>, '__doc__': None, '__slotnames__': []}


test_instance = restored_absolute() #Hello    ??????
print(test_instance) #<__main__.Absolute object at 0x0000024E30433230>
print(test_instance.__dict__) # {'data': 'Hi'}


# 4    ---------------------------------------------------
def fibonacci_with_pickle_saving(limit):
    pass
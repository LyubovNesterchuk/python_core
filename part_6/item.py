from pathlib import Path

class Item:

    pay_rate = 0.8
    all_class_instance = []
    class_instancess ={}

    def __init__(self, name: str, price: float, quantity=0):
        # assert у Python — це перевірка умови під час виконання програми. 
        # Якщо умова False, програма одразу падає з помилкою
        # assert умова, "повідомлення про помилку"
        # assert → для розробника (debug) raise → для користувача / реальної логіки
        try:
            assert price >= 0, f"Price {price} is not greater or equal to zero" # контроль внесення даних в систему
            assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero"
        except AssertionError:
            price = abs(price) # -1300 -> 1300
            quantity = abs(quantity)

        #self._name = name # protected викличе виняток, якщо при доступі не вказати одне нижнє підкреслення
        # self.__own_name = name # private для доступу та запису використовуємо get set
        self.name = name
        self.price = price
        self.quantity = quantity
        self.new_price = None

        Item.all_class_instance.append(self)

    # def get_name(self):
    #     return self.__own_name
    
    # def set_name(self, value):
    #     return self.__own_name == value

    def calculate_total_price(self):
        if self.new_price is None:
            return self.price * self.quantity
        return self.new_price * self.quantity

    def apply_discount(self):
        #self.new_price = self.price * self.pay_rate
        self.price = self.price * self.pay_rate #це знищує початкову ціну
    
    def info(self):
        return f"Item (name: {self.name}, price: {self.price}, quantity: {self.quantity})"
    
    @classmethod
    def all_items_info(cls):
        return [item.info() for item in cls.all_class_instance]
    
    # @classmethod
    # def load_data_from_csv(cls):
    #     with open(Path(__file__).parent / "item.csv", "r") as file:
    #         for item in file:
    #             print (item)
    #             name, price, quantity = item.strip().split(',')

    @classmethod
    def load_data_from_csv(cls):
        cls.all_class_instance.clear()  # очищення

        path = Path(__file__).parent / "item.csv"

        with open(path, "r") as file:
            next(file)
            for line in file:
                
                try:
                    name, price, quantity = line.strip().split(',')
                    cls(
                    # Item(
                        name = name.strip('"'),
                        price = float(price),
                        quantity = int(quantity)
                    )
                   

                except ValueError:
                    print("Помилка в рядку:", line)


Item.load_data_from_csv()
print(Item.all_items_info()) #['Item (name: "laptop", price: 50000.0, quantity: 5)', 'Item (name: "mobile", price: 12000.0, quantity: 12)', 'Item (name: "cable", price: 20.0, quantity: 14)', 'Item (name: "mouse", price: 7.0, quantity: 24)', 'Item (name: "keybord", price: 300.0, quantity: 2)', 'Item (name: Phone, price: 512.0, quantity: 2)', 'Item (name: mobile, price: 2000, quantity: 4)']


item = Item("Phonemobile",345, 134)

#Item.all_class_instance ніколи не очищається → кожен виклик додає ще дані

print(Item.all_items_info()) #'Item (name: laptop, price: 50000.0, quantity: 5)', 'Item (name: mobile, price: 12000.0, quantity: 12)', 'Item (name: cable, price: 20.0, quantity: 14)', 'Item (name: mouse, price: 7.0, quantity: 24)', 'Item (name: 
#keybord, price: 300.0, quantity: 2)', 'Item (name: Phonemobile, price: 345, quantity: 134)', 'Item (name: laptop, price: 50000.0, quantity: 5)', 'Item (name: mobile, price: 12000.0, quantity: 12)', 'Item (name: cable, price: 20.0, quantity: 14)', 'Item (name: mouse, price: 7.0, quantity: 24)', 'Item (name: keybord, price: 
#300.0, quantity: 2)', 'Item (name: Phone, price: 512.0, quantity: 2)', 'Item (name: mobile, price: 2000, quantity: 4)']



item = Item("Phone", 1000, 2)
print(item.calculate_total_price()) # 2000

print(item.pay_rate) # 0.8
print(item.__dict__) # {'name': 'Phone', 'price': 1000, 'quantity': 2}


item2 = Item("mobile", 2000, 4)
item2.pay_rate = 0.6
print(item2.__dict__)#{'name': 'mobile', 'price': 2000, 'quantity': 4, 'pay_rate': 0.6}
print(item2.pay_rate) # 0.6
print(item.pay_rate) # 0.8


item.apply_discount()
print(item.calculate_total_price()) #1600
item.apply_discount()
print(item.calculate_total_price()) #1280
item.apply_discount()
print(item.calculate_total_price()) #1024
print(item.info()) # Item (name: Phone, price: 512.0, quantity: 2)

print(Item.all_items_info())# ['Item (name: Phone, price: 512.0, quantity: 2)', 'Item (name: mobile, price: 2000, quantity: 4)']

Item.pay_rate = 0.9
item2 = Item("mobile", 2000, 4)
print(item2.__dict__)#{'name': 'mobile', 'price': 2000, 'quantity': 4, 'new_price': None}
print(item2.pay_rate) # 0.9
print(item.pay_rate) # 0.9
item2.apply_discount()
print(item2.calculate_total_price()) #7200.0



class Phone(Item):
    def __init__(self, name: str, price: float,broken_phones: int, quantity=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
    
    def info(self):
        return (f"Phone (name: {self.name}, price: {self.price}, "
                f"quantity: {self.quantity}, broken_phones: {self.broken_phones})")
    
phone = Phone(name="Nokia", price=12.4, broken_phones=3, quantity=7)

print(phone.__dict__)# {'name': 'Nokia', 'price': 12.4, 'quantity': 7, 'new_price': None, 'broken_phones': 3}
print(phone.info()) # Phone (name: Nokia, price: 12.4, quantity: 7, broken_phones: 3)
print(item.info()) # Item (name: Phone, price: 512.0, quantity: 2)

item =Item("Samsung", 2345, 34)

print(item.name)
print(item.info()) # Item (name: Samsung, price: 2345, quantity: 34)
item.apply_discount()
print(item.info()) # Item (name: Samsung, price: 2110.5, quantity: 34)
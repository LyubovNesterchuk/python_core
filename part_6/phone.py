from item import Item

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

item =Item("Samsung", 2345, 34)
print(item.info()) # Item (name: Samsung, price: 2345, quantity: 34)
item.apply_discount()
print(item.info()) # Item (name: Samsung, price: 2110.5, quantity: 34)
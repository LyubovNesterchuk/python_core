from datetime import datetime
from collections import UserList
class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str): 
       self.first_name = first_name
       self.last_name = last_name
       self.phone_number = phone_number
    
    def __str__(self):
       return f"{self.first_name} {self.last_name} | {self.phone_number}"
    
    def  __repr__(self):
        return str(self)

class Message:
    def __init__(self, content: str, author: User, recepient: User):
        self.content = content
        self.author = author
        self.recepient = recepient
        self.sending_time = datetime.now()
        self.receiving_time = None

    def is_message_read(self) -> bool:
        return self.receiving_time is not None

    def mark_message_as_read(self):
        self.receiving_time = datetime.now()

    def __str__(self):
       return f"Message from {self.author} to {self.recepient} | {self.content} {self.sending_time}"
    
    def  __repr__(self):
        return str(self)
    

class MessageSystem(UserList):

    def __init__(self, messages: list[Message] = []):
        super().__init__(messages)


    def get_messages_between_users(self, user_one: User, user_two: User):
        messages_set = set()
# 1) перебираємо усі повідомлення, які є у нашій системі
# 2) дістати інформацію про відправника та отримувача        
        for message in self:
            author, recepient = message.author, message.recepient
            if author == user_one and recepient == user_two:
                messages_set.add(message)
            if author == user_two or recepient == user_one:
                messages_set.add(message)

        return list(messages_set)
    

    def get_all_charts(self, user: User) -> list[User]:
        user_set = set() # множина має тільки унікальні значення
# 1) перебираємо усі повідомлення, які є у нашій системі
# 2) дістати інформацію про відправника та отримувача: коли користувач є автором, отримувачем, автором і отримувачем
        for message in self:
            author, recepient = message.author, message.recepient
            if user == author:
                user_set.add(recepient)
            if user == recepient and not user == author:
                user_set.add(author)

        return list(user_set)





user_lyubov = User("Lyubov", "Nest", "1234567890")
user_anna = User("Anna", "Nest", "0987654321")
user_nadya = User("Nadya", "Roma", "0987654211")

message_one = Message("Hello, Ann", user_lyubov, user_anna) 
message_two = Message("Hello, Lyubov", user_anna, user_lyubov)
message_three = Message("How are you?", user_lyubov, user_anna)

message_four = Message("Todo: finish homework", user_anna, user_anna)
message_five = Message("How are you?", user_lyubov, user_anna)


messages = [message_one, message_two, message_three, message_four]
message_system = MessageSystem(messages)
print(message_system.get_all_charts(user_anna)) # [Anna Nest | 0987654321, Lyubov Nest | 1234567890]
print(message_system.get_all_charts(user_lyubov)) # [Anna Nest | 0987654321]
print(message_system.get_messages_between_users)
from datetime import datetime
from collections import UserList
import json

MESSAGES_JSON_FILE = "messages.json"

class User:
    id = 0

    def __init__(self, first_name: str, last_name: str, phone_number: str): 
       User.id +=1
       self.id = User.id
       self.first_name = first_name
       self.last_name = last_name
       self.phone_number = phone_number


    def to_json(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }   
    
    def __str__(self):
       return f"{self.id} | {self.first_name} {self.last_name} | {self.phone_number}"
    
    def  __repr__(self):
        return str(self)



class Message:
    def __init__(self, content: str, author: User, recipient: User):
        self.content = content
        self.author = author
        self.recipient = recipient
        self.sending_time = datetime.now()
        self.receiving_time = None

    def is_message_read(self) -> bool:
        return self.receiving_time is not None

    def mark_message_as_read(self):
        self.receiving_time = datetime.now()

    def to_json(self) -> dict:
        return {
            "content": self.content,
            "sending_time": str(self.sending_time),
            "receiving_time": str(self.receiving_time),
            "author": self.author.to_json(),
            "recipient": self.recipient.to_json()
        }

    def __lt__(self, other) -> bool:
        return self.sending_time < other.sending_time

    def __str__(self):
       return f"Message from [{self.author}] to [{self.recipient}] \n '{self.content}' [{self.sending_time}]\n"
    
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
            author, recipient = message.author, message.recipient
            if author == user_one and recipient == user_two:
                messages_set.add(message)
            if author == user_two and recipient == user_one:
                messages_set.add(message)

        return sorted(list(messages_set))
    

    def save_to_file(self):
        with open(MESSAGES_JSON_FILE, "w") as json_file:
            json.dump(self.data, json_file, default = lambda o: o.to_json(), indent = 2)


    def read_from_json(self):
        users_dict ={}
        message_list = []

        with open(MESSAGES_JSON_FILE, "r") as json_file:
            json_data = json.load(json_file)
            for message_dict in json_data:
                author = None
                recipient = None
                author_id, recipient_id = message_dict["author"]["id"], message_dict["recipient"]["id"]
                
                if author_id in users_dict:
                    author = users_dict[author_id] 
                else:
                    author_dict =  message_dict["author"]
                    author = User(author_dict["first_name"], author_dict["last_name"], author_dict["phone_number"])
                    author.id = author_dict["id"]   
                    users_dict[author.id] = author

                if recipient_id in users_dict:
                    recipient = users_dict[recipient_id] 
                else:
                    recipient_dict =  message_dict["recipient"]
                    recipient = User(recipient_dict["first_name"], recipient_dict["last_name"], recipient_dict["phone_number"])
                    recipient.id = recipient_dict["id"]   
                    users_dict[recipient.id] = recipient

                message = Message(message_dict["content"], author, recipient)
                
                message.sending_time = datetime.fromisoformat(message_dict["sending_time"])
                if message_dict["receiving_time"] != "None":
                    message.receiving_time = datetime.fromisoformat(message_dict["receiving_time"])
                
                message_list.append(message)   
        
        return message_list
        
    def __eq__(self, other):
        return self.sending_time == other.sending_time and self.content == other.content

    def __hash__(self):
        return hash((self.sending_time, self.content))

    def get_all_chats(self, user: User) -> list[User]:
        user_set = set() # множина має тільки унікальні значення
# 1) перебираємо усі повідомлення, які є у нашій системі
# 2) дістати інформацію про відправника та отримувача: коли користувач є автором, отримувачем, автором і отримувачем
        for message in self:
            author, recipient = message.author, message.recipient
            if user == author:
                user_set.add(recipient)
            if user == recipient and not user == author:
                user_set.add(author)

        return list(user_set)





user_lyubov = User("Lyubov", "Nest", "1234567890")
user_anna = User("Anna", "Nest", "0987654321")
user_nadya = User("Nadya", "Roma", "0987654211")
# print(user_lyubov)
# print(user_anna)
# print(user_nadya)
# print(User.id)

message_one = Message("Hello, Ann", user_lyubov, user_anna) 
message_two = Message("Hello, Lyubov", user_anna, user_lyubov)
message_three = Message("How are you?", user_lyubov, user_anna)

message_four = Message("Todo: finish homework", user_anna, user_anna)

message_five = Message("How are you?", user_lyubov, user_nadya)
message_six = Message("OK. And you?", user_nadya, user_lyubov)

messages = [message_one, message_two, message_three, message_four, message_five, message_six]
message_system = MessageSystem(messages)

message_system.save_to_file()

print(message_system.get_all_chats(user_anna)) # [Anna Nest | 0987654321, Lyubov Nest | 1234567890]
print(message_system.get_all_chats(user_lyubov)) # [Anna Nest | 0987654321]
print(message_system.get_messages_between_users)

message_system = MessageSystem()
print(message_system.read_from_json())
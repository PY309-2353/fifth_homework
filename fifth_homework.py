# coding=utf-8
class Client:
    id = 0

    def __init__(self, surname, name, middle_name, age, money_ammount=0.0):
        self.unique_id = Client.id + 1
        Client.id += 1
        self.surname = surname
        self. name = name
        self.middle_name = middle_name
        self.age = age
        self.money_ammount = money_ammount

        
    def add_money(self, ammount):
        self.money_ammount += ammount
    def withdraw_money(self, ammount):
        self.money_ammount -= ammount

    def send(self, ammount, Client):
        Client.money_ammount += ammount


client1 = Client('Колков', 'Кирилл', 'Викторович', 39)
client2 = Client('Петров', 'Алексей', 'Васильевич', 24)
client3 = Client('Петров', 'Алексей', 'Васильевич', 24)

print(client1.unique_id)
print(client2.unique_id)
print(client3.unique_id)




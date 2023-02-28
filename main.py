"""Создаём класс Client с атрибутами Имя, Фамилия, Город, Баланс"""
class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    """С помощью магического метода __str__ создаём вывод в строку атрибутов"""
    def __str__(self):
        return f'<<{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб.>>'
    """Создаём функцию которая ограничивает вывод только 3х необходимых атрибутов"""
    def get_guest(self):
        return f'{self.name} {self.surname},г. {self.city}'

"""Формируем список клиентов"""
client_1 = Client('Иван','Петров','Москва',50)
client_2 = Client('Пётр','Иванов','Нижний Новгород',120)
client_3 = Client('Сергей','Ерёмин','Семёнов',2)

"""Создаём список клиентов приглашённых на вечеринку"""
guest_list=[client_1,client_2,client_3]

"""Производим вывод в консоль информации о клиентах приглашённых на вечеринку"""
for guest in guest_list:
    print(guest.get_guest())

"""Производим вывод в консоль информации о клиенте 1 из функции __str__ c полным списком атрибутов"""
print(client_1)

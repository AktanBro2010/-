""" ООП - Объектно Ориентрованное Программирование """


# ООП -  способ написания кода. Два основных понятия: классы и объекты

# Классы - блок кода, который описывает объекты: свойства/атрибуты, методы/функции

# Объекты - экземпляры/переменные, которые относятся к указанному классу


# class MyClass:
#     ...

# obj = MyClass()


# num = 10
# num = int(10)


# class Human:
#     hands = 2
#     leg = 2
#     head = 1
#     eyes = 2
#     hair = 'black'
#     # атрибуты/свойства класса

#     def eat(self): # метод - функция внутри класса
#         print('Human eating')


# human1 = Human()
# print(human1.leg)  # 2

# human1.eat()  
# # одно и то же
# Human.eat(human1)

# human1.hands = 1
# human1.eyes -= 1

# print(human1.hands)
# print(human1.eyes)

# human1.tail = 1
# print(human1.tail)

# human1.phone  # AttributeError


# class Laptop:
#     keyboard = True
#     touchpad = True
#     # атрибуты класса

#     def __init__(self, title, price, color, ram, ds):
        # атрибуты экземпляра/объекта
#         self.title = title
#         self.price = price
#         self.color = color
#         self.ram = ram
#         self.display = ds
#         print('__init__ сработал')

#     def set_radio(self):
#         self.radio = True

#     def set_ram(self, value):
#         print(self.ram)
#         self.ram = value

# __init__ - метод для создания объектов


# l1 = Laptop('Asus', 10000, 'silver', 1024, '13.5')
# l2 = Laptop('Apple', 12000, 'black', 256, '15.6')

# l1.set_radio()
# l1.radio

# l1.price = 500
# l2.price  # 1234

# l1.keyboard = False
# print(l2.keyboard)

# Laptop.touchpad = False

# print(l1.touchpad)

# l2.set_ram(512)
# одно и то же
# Laptop.set_ram(self=l2, value=512)


# class Phone:
#     phone_counter = 0

#     def __init__(self):
#         Phone.phone_counter += 1
#         print(f"Сейчас {Phone.phone_counter} объектов")
        

# p1 = Phone()
# p2 = Phone()
# p3 = Phone()


# Классы бывают:
# Функциональные классы - классы для хранения действий (методов/функций)
# Датаклассы - для хранения данных (свойств/атрибутов)


# class Car:
#     def __init__(
#             self,
#             color: str,
#             mark: str,
#             model: str,
#             engine: bool = True,
#     ):
#         self.color = color
#         self.mark = mark
#         self.model = model
#         self.engine = engine


# from dataclasses import dataclass

# @dataclass
# class Car:
#     model: str
#     engine: bool = True
#     mark: str
#     color: str


# car = Car('BYD', True, 'e50', 'white')
# car.color


# dict_car = {
#     'mark': ...,
#     'color': ...
# }
# dict_car[colok]


class Mebel:
    __slots__ = ('height', 'width', 'color')

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

table = Mebel(20, 30, 'white')
# table.tail = True

isinstance(table, Mebel)  # True
isinstance('string', int)  # False


""" 
Наследование
Инкапсуляция
Полиморфизм

Абстракция
Ассоциация (Агренация, Композиция)
"""
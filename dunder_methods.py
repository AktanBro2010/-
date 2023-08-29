""" 
Магические методы (dunder - double underscore) 
"""

# __init__, __str__

# 1. __new__() - конструктор класса, отвечает за создание объекта

# 2. __init__()

# 3. __del__() - деструктор, отвечает за удаление объекта


from typing import Any


class Point:

    def __new__(cls, *args, **kwargs):
        print('Вызов метода new')
        super().__new__(cls)

    def __init__(self, x, y):
        print('init')
        self.x = x
        self.y = y

    def __del__(self):
        print('удаление экземпляра' + str(self))

# a = Point(4, 5)
# print(a)


class Word(str):
    def __new__(cls, *args: str):
        string = args[0].replace(' ', '')
        return str.__new__(cls, string)
    

# string = Word('He   llo')
# print(string)


class User:
    def __new__(cls, name, age):
        if age < 18:
            raise ValueError(
                'Вы слишком молоды'
            )
        return object.__new__(cls)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name

# admin = User('Admin', 18)
# print(admin)

# import datetime

# print(repr(datetime.date.today()))
# print(datetime.date.today())
# c = repr(datetime.date.today())
# print(eval(c))

# a = datetime.date.today()
# print(a)
# print(eval(a))


class MyNumber(int):
    def __init__(self, value):
        self.value = value

    def __add__(self, value2):
        return f'Это сложение, и сумма равна: {self.value + value2}'
    
    def __sub__(self, value3):
        return f'Это вычитание, и разность равна: {self.value - value3}'

    def __mul__(self, value4):
        return f'Это умножение, и произведение равно: {self.value * value4}'
    
    def __truediv__(self, value5):
        return f'Это деление, и частное равно: {self.value / value5}'
    
    def __floordiv__(self, value6):
        return f'Это целочисленное деление, и частное равно: {self.value // value6}'
    
    def __pow__(self, value7):
        return f'Результат возведения {self.value} в {value7} степень: {self.value ** value7}'
    
    def __mod__(self, value8):
        return f'Остаток от деления: {self.value % value8}'


# int_obj = MyNumber(9)
# print(int_obj + 7)
# print(int_obj - 7)
# print(int_obj * 7)
# print(int_obj / 7)
# print(int_obj // 7)
# print(int_obj ** 7)
# print(int_obj % 7)


# == - __eq__(self, value) - equal - равно
# != - __ne__(self, value) - not equal - не равно
# > - __gt__(self, value) - greater than - больше
# < - __lt__(self, value)
# >= - __ge__(self, value)
# <= - __le__(self, value)


class Base:
    def __init__(self, string):
        self.string = string

    def __invert__(self):  # ~ - переворачивает итерируемый объект
        return self.string[::-1]
    
    def __str__(self) -> str:
        return self.string
    

# i = Base('Hello world')
# res = ~i
# print(res)


# __getattribute__(self, item(атрибут, к которому идет обращение)) - автоматически вызывается при обращении к атрибутам (получение свойства объекта)

# string = 'hello'
# print(string.lower)
# print(string.__getattribute__('lower'))

# __getattr__ - вызывается автоматически при обращении к не существующему атрибуту

# __setattr__ - вызывается автоматически при присвоении атрибуту нового значения

# __delattr__ - вызывается автоматически при удалении атрибута


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, name):
        print('__getattribute__')
        # if name == 'x':
        #     raise ValueError(
        #         'Доступ запрещён!'
        #     )
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value):
        print('__setattr__')
        super().__setattr__(name, value)

    def __getattr__(self, name):
        print('__getattr__')
        # raise AttributeError(
        #     'No such attribute'
        # )

    def __delattr__(self, name):
        print('__delattr__')
        super().__delattr__(name)


p = Point(8, 0)

del p.x

# p.x
# p.z
# p.x = 9


# __getitem__ - по ключу, по индексу или делаете срез
# __setitem__ - создается ключ с каким-то значением
# __delitem__ - удаление по ключу, индексу
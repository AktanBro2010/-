""" Методы """

# 1. методы экземпляра (instance methods)
# 2. методы класса (class methods)
# 3. статические методы (static methods)


# Методы экземпляра(объекта)
# обычные, которые принимают первым аргументом self (для работы с атрибутами)

class A:
    def __init__(self, a):
        self.a = a

    def instance_method(self):
        print('Метод объекта')

# a = A(1)
# a.instance_method() - 1 способ
# A.instance_method(a) - 2 способ
# A.a
# a.a


# Методы класса - принимают первым аргументом ссылку на класс (cls). Нужны для создания объекта, изменения атрибута класса. Для создания используется декоратор @classmethod (вызываются и через объект, и через класс)

class B:
    @classmethod
    def class_method(cls):
        print('Метод класса')

# obj = B()
# obj.class_method()
# B.class_method()


class Car:
    color = 'red'

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color

    # def change_color(self, new_color):
    #     self.color = new_color

# lada = Car()
# bmw = Car()
# lada.change_color('black')
# print(lada.color, bmw.color)
# Car.change_color(bmw, 'gray')
# print(Car.color)


class Counter:
    c = 0

    def __init__(self):
        self._increase()

    def __del__(self):
        self._decrease()
        del self

    @classmethod
    def _increase(cls):
        cls.c += 1

    @classmethod
    def _decrease(cls):
        cls.c -= 1
        

# obj1 = Counter()
# obj2 = Counter()
# obj3 = Counter()
# del obj1
# del obj2
# del obj3
# print(Counter.c)


class Pizza:
    def __init__(self, raduis, *ingredients):
        self.radius = raduis
        self.ingredients = ingredients

    def cook(self):
        print(f'Готовится пицца размером {self.radius * 2} см')
        print(f'Ингредиенты: {self.ingredients}')

    @classmethod
    def chilli(cls, r):
        pizza = cls(r, 'перец', 'фарш', 'сыр Моцарелла', 'острый перец', 'сыр Голландский')
        return pizza

# pizza1 = Pizza(15, 'колбаса', 'сыр')
# pizza1.cook()

# pizza_chilli = Pizza.chilli(20)
# print(pizza_chilli)
# pizza_chilli.cook()


# Статические методы - не принимают в себя ссылку на класс и на объект. Просто функции внутри класса (которые не взаимодействуют с классом и объектом). Используются только внутри класса. Для создания используют декоратор @staticmethod (изменение типа данных, расчеты и т.д.)

class C:
    @staticmethod
    def static_method(x, y):
        print(x + y)

# C.static_method(2, 4)
# c = C()
# c.static_method(5235435235, 4395285435)


class Cylinder:
    def __init__(self, diametr, height):
        self.diametr = diametr
        self.height = height
        self.area = self.get_area(diametr, height)

    @staticmethod
    def get_area(d, h):
        from math import pi
        circle = pi * d ** 2 / 4
        side = pi * d * h
        area = circle * 2 + side
        return round(area, 2)
    

# print(Cylinder.get_area(4, 2))
# cylinder = Cylinder(2, 8)
# print(cylinder.area)


class Home:
    count_people = 0

    def __init__(self, name, last_name, count_people2):
        self.name = name
        self.last_name = last_name
        self.count_people = count_people2
        Home.count_people += count_people2

    def info(self):
        print(self.name, self.last_name)
        
    @classmethod
    def f(cls):
        print(cls.count_people)

    @staticmethod
    def about_home():
        print('Лучший дом, покупайте квартиры!  НЕДОРОГО!!!')


# kv1 = Home('Петр', 'Стельмах', 13)
# kv2 = Home('Айкол', 'Сергекбеков', 2)
# print(kv1.count_people)
# kv1.f()
# kv2.about_home()


class Iphone14:
    cost = 120000

    def __init__(self, money, name):
        if money < Iphone14.cost:
            a = self.get_money(money, Iphone14.cost)
            raise Exception(f'Вам не хватает {a} сом')
        self.owner = name

    @classmethod
    def change_cost(cls, new_cost):
        cls.cost = new_cost

    @staticmethod
    def get_money(money, cost):
        return cost - money


i = Iphone14(5000, 'Aktan')
i.change_cost(80000)
print(Iphone14.cost)



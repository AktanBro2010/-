""" Основные принципы ООП: Инкапсуляция """

# 1. Объединение всего в одну капсулу(класс)
# 2. Ограничение доступа к атрибутам и методам - сокрытие данных от внешнего воздействия

# Инкапсуляция как связь

class Phone:
    number = '+996705435434'

    def print_number(self):
        print(f'Мой номер: {self.number}')


# my_phone = Phone()
# my_phone.print_number()


# Инкапсуляция как управление доступа

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# pt = Point(12, 4)
# print(pt.x, pt.y)
# pt.x = 'hello'


""" Три модификатора доступа """
# 1. public - публичный (без нижних подчеркиваний) -> x, y, z
# 2. _protected - защищенный (с одним подчеркиванием), доступны внутри класса и у дочерних -> _x, _y, _z
# 3. __private - приватный (с двумя подчеркиваниями)

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

# pt = Point(1, 2)
# print(pt._x, pt._y)


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y

    def set_coords(self, new_x, new_y):
        if type(new_x) in (int, float) and type(new_y) in (int, float):
            self.__x = new_x
            self.__y = new_y
        else:
            raise ValueError('Координаты должны быть числами')
        

# pt = Point(1, 2)
# pt.get_coords()
# pt._Point__x = 'test'
# pt.set_coords(5, 99)
# print(pt.__dict__)
# pt._Point__y = 'hello'
# print(pt.__x, pt.__y)


""" 
getter & setter - методы, через которые предполагается работа с защищенными данными.
Они используются для получения и установки значений, чтобы добавить логику проверки при получении или задании данных.
"""

class P(Point):
    pass

p = P(4, 10)
# print(p.get_coords())
# print(p.__dict__)
# print(p._Point__x)


class Solution:
    __private = 321

    def __private_method(self):
        print('Это приватный метод')

    def method(self):
        print(f'{self.__private} - приватная переменная')
        self.__private_method()

# s = Solution()
# s.method()


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def get_age(self):  # getter
        return self.__age
    
    def set_age(self, new_age):  # setter
        if type(new_age) in (int, float) and new_age in range(0, 101):
            self.__age = new_age
        else:
            raise ValueError('Возраст должен быть числом, не меньше 0 и не больше 100!')
        
# man = Person('Michael')
# man.set_age(23)
# print(man.get_age)


# @property - позволяет к методу обращаться как к атрибуту, @свойство.setter


class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if type(new_age) in (int, float) and new_age in range(0, 101):
            self.__age = new_age
        else:
            raise ValueError('Invalide age')
        
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise ValueError('You can\'t delete age')
        
        del self.__age


# man = Person('Trevor')

# man.age = 99
# del man.age
# print(man.age)


class Kyrgyzstan:
    __name = 'Kyrgyz Republic'
    __population = 0

    @property
    def population(self):
        return f'{self.__population} - население {self.__name}'
    
    @population.setter
    def population(self, pop):
        if isinstance(pop, (int, float)) or pop in range(1000, 10000001):
            self.__population = pop
        else:
            raise ValueError('Invalide population')
        

# country = Kyrgyzstan( 
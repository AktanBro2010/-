""" Основные принципы ООП: Полиморфизм """

""" Разное поведение одного и того же метода в разных классах """

# list.pop()
# dict.pop()
# set.pop()

# +
# 4 + 5
# 'str' + 'str1'
# [1, 2, 3] + [4, 5, 6]

# len()
len('string')
len([1, 2, 3, 4, 5])
...


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'This dog has name {self.name}.')

    def make_sound(self):
        print('meow')


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'This cat has name {self.name}')

    def make_sound(self):
        if self.name == 'Barsik':
            print('Gav')
        else:
            print('Rav')


# animals = [Dog('Muhtar', 2), Dog('Boss', 1), Cat('Barsik', 4), Cat('Murka', 6)]

# for i in animals:
#     i.info()
#     i.make_sound()


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def get_areat(self):
        pass

    def fact(self):
        return 'Я фигура в двухмерной плоскости'

    def __str__(self):
        return self.name
    

class Square(Shape):
    def __init__(self, length):
        super().__init__('Square')
        self.length = length

    def get_area(self):
        return self.length ** 2
    
    def fact(self):
        return 'У квадрата все стороны равны'
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__('Circle')
        self.radius = radius

    def get_area(self):
        return round(pi * self.radius ** 2)
    
    def fact(self):
        return 'У круга нет начала и конца'
    

# shapes = [Square(4), Square(8), Circle(3), Circle(8)]

# for i in shapes:
#     print(i.fact())
#     print(i.get_area())


# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядить батарею

class MobilePhone:
    def __init__(self, imei='7435747653', os='IOS 1.17', battery=80):
        self.__imei = imei
        self.__battery =  battery
        self.__os = os

    def check_battery(self, b_l=0.5, b_l2=0.5):
        if self.__battery < b_l:
            raise(ValueError('Телефон разряжен, все методы не будут доступны до зарядки'))
        self.__battery -= b_l2

    @property
    def battery_level(self):
        self.check_battery()

    @property
    def info(self):
        self.check_battery()
        print(f'os: {self.__os}\nIMEI: {self.__imei}\nbattery_level: {self.__battery}')

    def music(self):
        self.battery_level(5, 5)

    def video(self):
        self.battery_level(10, 7)
        self.__battery -= 0.5
        
    def add_battery(self, min):
        from datetime import datetime, timedelta
        from time import sleep

        now = datetime.now
        end_time = (now() + timedelta(minutes=min)).strftime('%M:%S')
        while now().strftime('%M:%S') != end_time:
            sleep(5)
            if self.__battery < 100:
                self.__battery += 1
            else:
                break
            print(f'Идет зарядка батареи! Ваш текущий уровень заряда: {self.__battery}')


phone = MobilePhone()
phone.battery_level
phone.info
phone.music()
phone.add_battery(12)



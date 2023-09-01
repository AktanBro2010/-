""" 
Абстракция - принцип ООП, в котором создается класс пустышка, где задаются названия атрибутов и методов, для определения их в дочерних классах 
"""


from abc import ABC, abstractmethod, abstractproperty

class A(ABC):
    def method(self):
        print('Обычный метод')

    @abstractproperty
    def test(self):
        pass

    @abstractmethod
    def method2(self):
        print('Абстрактный метод')  # обычно не определяют логику. Будет обязательным для переопределения в дочернем классе

class B(A):
    # test = 4

    def test(self):
        pass
    # method2 = 9
    # def method2(self):
    #     print('переопредилим')


# b = B()

# a = A()  # нельзя создать объект от абстрактного класса, в котором есть абстрактный метод


# class AbstractAnimal(ABC):

#     @abstractproperty
#     def paw(self):
#         pass

#     @abstractmethod
#     def voice(self):
#         pass


# class Dog(AbstractAnimal):
#     paw = 4

#     def voice(self):
#         print('гав гав')


# dog = Dog()


class Abst(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def set_info(self):
        pass


class IdenticateMixin:
    def identicate(self, year):
        if int(year) < 2010:
            return 'This is old car'
        return 'This is a new car'


class Auto(IdenticateMixin, Abst):
    def __init__(self, model, year, owner):
        self.model = model
        self.year = year
        self.__owner = owner

    def get_info(self):
        return f'model: {self.model}\nyear: {self.year}'
    
    def set_info(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
    

# auto = Auto('Mercedes', 2023, 'Ильяс')

# print(auto.get_info())

# print(auto.get_owner())

# auto.set_info('Петр')

# print(auto.identicate(auto.year))


# class Kamaz(IdenticateMixin, Abst):
#     get_info = 0
#     set_info = 0


class Abst(ABC):
    
    @abstractmethod
    def info(self):
        pass


class FacMixin:
    def check(self, faculty):
        if 'IT' in faculty:
            return 'cool'
        else:
            return 'not bad'


class Student(FacMixin, Abst):
    def __init__(self, name, last_name, faculty, class_):
        self.name = name
        self.last_name = last_name
        self.faculty = faculty
        self.__class_ = class_

    def info(self):
        return f'name: {self.name}\nlast name: {self.last_name}\nfaculty: {self.faculty}'
    
    @property
    def _class(self):
        return self.__class_

    def class_(self, class_):
        self.__class_ = class_


student = Student('Emirlan', 'Janykulov', 'IT company', '2')

# print(student.info())

# print(student.proverka())

print(student.class_('3'))

print(student.info())

print(student._Student__class_)

print(student.check(student.faculty))
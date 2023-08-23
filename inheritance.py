""" 
Основные принципы ООП: Наследование 
"""

# Наследование - принцип ООП, в котором мы можем унаследовать, 
# переопределить и использовать в дочернем классе все атрибуты и методы родительского класса. 

# Создаем новый класс на основе уже существующего


# class parent_class:
    # методы и атрибуты родительского класса

# class daughter_class(parent_class):
    # методы и атрибуты дочернего класса


class Animal:
    def say(self):
        print('I\'m animal')

class Croco(Animal):
    pass

# croco = Croco()
# croco.say()
# print(dir(Croco))


# class A:
#     def method(self):
#         print('Метод в классе A')

# class B:
#     name = 'B'
#     def method(self):
#         print('Метод в классе B')

#     def method_b(self):
#         print('Hello world')

# class C(A):
#     pass


# b = B()
# b.method()
# c = C()
# c.method()

# mro - (Method resolution order) - порядок поиска атрибутов и методов

# print(B.__mro__)
# одинаково, но сверху возвращает кортеж, а снизу - список
# print(B.mro())


""" Виды наследований """
# 1. Одиночное наследование - когда мы наследуемся только от 1-го родителя
# 2. Иерархическое наследование - когда у одного родителя много дочерних классов
# 3. Многоуровневое наследование - когда мы наследуемся от класса, у которого уже есть родитель
# 4. Множественное наследование - когда у одного дочернего класса несколько родительских классов
# 5. Гибридное наследование - когда используются несколько видов наследования


class Person:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f'Name: {self.name} \nLast name: {self.last_name} \nAge: {self.age}')


class Employee(Person):
    def work(self):
        print(f'{self.name} is working')


class Student(Person):
    # def __init__(self, name, last_name, age, faculty):
    #     self.name = name
    #     self.last_name = last_name
    #     self.age = age
    #     self.faculty = faculty

    # def __init__(self, name, last_name, age, faculty):
    #     Person.__init__(self, name, last_name, age)
    #     self.faculty = faculty

    def __init__(self, name, last_name, age, faculty):
        super().__init__(name, last_name, age)
        self.faculty = faculty

    def study(self):
        print(f'{self.name} is studying')

# e = Employee('Jake', 'Norway', 20)
# e.work()
# e.display_info()

# s = Student('Mary', 'Poker', 17, 'IT')
# s.study()
# s.display_info()


class A:

    def my_range(self, number):
        list(range(number+1))
        return [i for i in range(number+1)]

a = A()
# print(a.my_range(12))


class B(A):
    def my_range(self, number):
        super().my_range(number)
        return f'Вы сделали список от 1 до {number}'
    
    def __str__(self):
        ...
        # return f'{self.number}'



# b = B()
# print(b.my_range(12))


# issubclass() - проверяет, является ли класс A дочерним классом класса B

# print(issubclass(A, B))  # True
# print(issubclass(B, A))  # False
# print(issubclass(A, object))  # True


# class MyString(str):
#     pass

# print(dir(MyString))


# class MyString(str):
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return f'{self.string}'

#     def append(self, str):
#       self.string += str

#     def pop(self):
#         list(self.string).pop(-1)

# st = MyString('Hello')
# st.pop()


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def describe_user(self):
        print(f'{self.username} -> {self.email}')

    def greet_user(self):
        print(f'Welcome, {self.username}')


class AdminUser(User):

    def __init__(self, username, email, password):
        super().__init__(username, email, password)
        self.privileges = []

    def __str__(self):
        return 'admin'
    
    def add_privileges(self, privil):
        self.privileges.append(privil)

    def show_privileges(self):
        print(self.privileges)


user = AdminUser('Shon', 'shonbek_uzbek@uzbek.uz', 'Shonbek')
user.add_privileges('delete posts')
user.show_privileges()
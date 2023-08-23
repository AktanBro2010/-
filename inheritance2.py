""" Множественное наследование """

class Lion:
    color = 'black'


class Lioness:
    color = 'brown'


class Child(Lion, Lioness):
    pass

obj = Child()
# print(obj.color)  # black

# print(Child.__mro__)

# mro


class Grandpa:
    def sleep(self):
        print("I'm sleeping")


class Grandma:
    def cook(self):
        print("I'm cooking")


class Father(Grandpa, Grandma):
    last_name = 'Parker'

    def work(self):
        print("I'm working")


class Mother(Grandpa):
    last_name = 'Smith'


class Child(Father, Mother):
    pass

# Child, Father, Mother
# print(Child.__mro__)
# c = Child()
# print(dir(c))5


""" Проблемы множественного наследования """

# 1. Проблема Ромба - решение при помощи mro

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# D B A C A - раньше(в один класс заходили два раза)
# D B C A - сейчас(благодаря mro)


""" Проблема перекрестного (скрещенного) наследования - НЕ РЕШЕНА! """

# class A:
#     ...

# class B:
#     ...

# class C(A, B):
#     ...

# class D(B, A):
#     ...

# class E(C, D):
#     ...


class MoveMixin:
    def move(self, pos_x, pos_y):
        self.validate_values(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y


class Square:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y

    def validate_values(self, x, y):
        if type(y) and type(x) not in (int, float):
            raise ValueError('Координаты должны быть числом!')
        

    def move(self, pos_x, pos_y):
        self.validate_values(pos_x, pos_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, size_x, size_y):
        self.validate_values(self, size_x, size_y)
        self.size_x = size_x
        self.size_y = size_y


class Triangle(Square):
    ...

# print(dir(Triangle))


""" Mixin - классы, которые используются только для наследования, и не используются для создания объектов """

# Классы примеси

# Работа с Миксинами:
# 1. Принято давать имена, заканчивающиеся нa Mixin
# 2. Не принято создавать объекты
# 3. Нужны для расширения функционала другого класса


# class ManMixin:
#     def move(self):
#         print('Muchacho')


# class WomanMixin:
#     def stop(self):
#         print('Muchacha')


# class Person(ManMixin, WomanMixin):
#     pass

# class Car(ManMixin, WomanMixin):
#     pass

# class River(ManMixin):
#     pass
# for obj in [Car(), Car(), Person(), River()]:
#     obj.move()


class PersonInitMixin:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last = last_name
        self.age = age

class IncreaseAgeMixin:
    def add_year(self):
        self.age += 1


class Person(PersonInitMixin, IncreaseAgeMixin):
    ...

class Employee(PersonInitMixin, IncreaseAgeMixin):
    ...

class Student(PersonInitMixin, IncreaseAgeMixin):
    ...

# p = Person('Mike', 'Tyson', 23)
# p.add_year()
# print(p.age)


# class ToDo:
#     def create(self):
#         ...
#     def update(self):
#         ...
#     ...


class CreateMixin:
    def create(self, todo, key):
        if key in self.todos:
            return 'Задача под таким ключом уже существует'
        if todo in self.todos.values():
            return 'Такая задача уже существует'
        self.todos[key] = todo
        return self.todos


class DeleteMixin:
        def delete(self, key):
            if key in self.todos:
                deleted = self.todos.pop(key)
                return deleted
            return 'Такой задачи нет'
    

class UpdateMixin:
    def update(self, key, new_todo):
        self.todos[key] = new_todo    


class ReadMixin:
    def read(self):
        print(sorted(self.todos.items()))


class ToDO(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}

task = ToDO()
task.create('do homework', 1)
# task.delete(1)
task.update(1, 'read a book')
task.create('work', 2)
task.read()

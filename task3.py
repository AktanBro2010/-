# Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.
# Определите во всех трёх классах метод get_info():
# для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
# для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.
# для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.
# Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.
# Вызовите метод get_human_info у каждого экземпляра печатать результат.
# Ввод должен быть:
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.
# Определите во всех трёх классах метод get_info():
# для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
# для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.
# для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.
# Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.
# Вызовите метод get_human_info у каждого экземпляра печатать результат.
# Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.
# Определите во всех трёх классах метод get_info():
# для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
# для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.
# для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
# Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.
# Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.
# Вызовите метод get_human_info у каждого экземпляра печатать результат.
# Ввод должен быть:
# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 


class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return 'Привет, меня зовут Иван Петров'


class Employee(Person):
    def __init__(self, work, status):
        self.work = work
        self.status = status

    def get_info(self):
        return 'Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор'

      
class Student(Person):
    def __init__(self, university, course):
        self.university = university
        self.course = course

    def get_info(self):
        return 'Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе'
    

def get_human_info(person1):
    for person1 in :
        print(person1.get_info())


person = Person('Baike', 'Saike')
employee = Employee(' fds', 'fds')
student = Student('IT', 'mochno')


get_human_info(employee) 
get_human_info(student) 
get_human_info(person) 
""" 
Ассоциация - принцип, в котором два класса связаны друг с другом 
"""

# 1. Агрегация - слабая связь
# 2. Композиция - сильная связь


class A:  # Компонент
    pass

class B:  # составной
    # содержит объект от класса А
    pass


class Engine:
    ...

class Wheel:
    ...

class Elochka:
    ...

class Car:
    def __init__(self, elochka):
        self.elochka = elochka
        self.engine = Engine()
        self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]


# freshener = Elochka()

# car = Car(freshener)


# Агрегация
# class Salary:
#     def __init__(self, pay):
#         self.pay = pay

#     def get_total(self):
#         return self.pay * 12


# salary = Salary(30000)


# class Employee:
#     def __init__(self, pay: Salary, bonus):
#         self.pay = pay
#         self.bonus = bonus

#     def annual_salary(self):
#         print(f'total: {self.pay.get_total() + self.bonus}')

# emp = Employee(salary, 10000)
# emp.annual_salary()


""" Композиция """
class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


salary = Salary(30000)


class Employee:
    def __init__(self, pay: int, bonus: int):
        self.pay = Salary(pay)
        self.bonus = bonus

    def annual_salary(self):
        print(f'total: {self.pay.get_total() + self.bonus}')

# emp = Employee(30000, 10000)
# emp.annual_salary()


class Battery:
    _power = 100

    def charge(self):
        if self._power < 100:
            self._power = 100


class Iphone:
    def __init__(self, color, storage):
        self.color = color
        self.storage = storage
        self.battery = Battery()

    
class Nokia:
    def __init__(self, battery: Battery, color: str = 'Синий'):
        self.battery = battery
        self.color = color
        self.storage = 8

# battery = Battery()

# i = Iphone('black', 256)
# nokia = Nokia(battery)

# i.battery._power = 50
# i.battery.charge()
# print(i.battery._power)


class Employee:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def lecture(self):
        print(f'Провожу лекцию группе')
    
    def interactive(self):
        print(f'Провожу интерактив группе')



class Students:
    def __init__(self, name, last_name, age, email):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.kpi = 0

    def study(self):
        print('Просматриваю лекцию')
        self.kpi += 8

    def do_tasks(self):
        print('Решаю таски')
        self.kpi += 10

    def pass_test(self):
        self.kpi += 15


class Group:
    def __init__(self, name, count_students):
        self.name = name
        self.count_students = count_students
        self.mentor = Employee('Aigerim', 'Taalaibekovna', )
        
junPYpack = Group('junPYpack', 17)
pitHUB = Group('pitHUB', 15)


class Cabinet:
    def __init__(self, number, seats, group1, group2=None):
        self.number = number
        self.seats = seats
        self.group = [group1, group2]    

cab_9 = Cabinet(9, 35, junPYpack, pitHUB)
print(cab_9.group[0].mentor.name)

class Makers:
    def __init__(self, cab_count: int, *employees):
        self.employees = [employees]
        self.cabinets = cab_count
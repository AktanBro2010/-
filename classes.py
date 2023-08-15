""" ООП """

class A(object):
    b = 2  # атрибут класса

    def __init__(self, c, d):  # атрибуты объекта (экземпляра класса)
        self.c = c
        self.d = d
    
# a = A(3, 4)
# a.e = 5
# print(a)


class Salary:
    nalog = 15

    def __init__(self, zp, staj):
        self.zp = zp
        self.staj = staj

    def sum_nalog(self):
        return (self.zp * self.staj) * (self.nalog / 100)
    
# summa = Salary(100000, 2)
# print(summa.sum_nalog())


class Car:
    def __init__(self, owner: str, model: str, year: int, mileag = 0, is_going = False):
        self.owner = owner
        self.model = model
        self.year = year
        self.mileag = mileag
        self.is_going = is_going

    def go(self, way):
        print('You are in way')
        self.mileag += way
        self.is_going = True
    
# car = Car('Aktan', 'Lamborghini Aventador', 2020)
# car.go(200)
# print(car.mileag)


class SelfBank:

    total = 0
    
    def add_sum(self, add: int):
        self.total += add
    
    def get_total_sum(self):
        print(f'Ваш баланс {self.total} сом.')

    def sub_sum(self, out: int):
        if out > self.total:
            raise Exception(
                'Недостаточно средств')
        else:
            self.total -= out

# account = SelfBank()
# account.add_sum(1323)
# account.get_total_sum()
# account.sub_sum(1600)


class Student:
    def __init__(self, name, last_name, book = [], knowledge = 0, is_ready_to_work = False, languages = {}):
        self.name = name
        self.last_name = last_name
        self.book = book
        self.knowledge = knowledge
        self.is_ready = is_ready_to_work
        self.languages = languages

    def read_book(self, book):
        self.book.append(book)
        self.add_points(100)

    def do_home_work(self):
        self.add_points(30)

    def do_real_project(self):
        self.add_points(200)

    def learn_new_language(self, lang: str, point):
        if 0 < point < 100:
            self.languages.update({lang: point})
        else:
            raise Exception(
                'Ваши баллы выходят за пределы доступного'
            )
        self.add_points(20)

    def add_points(self, points):
        self.knowledge += points

        if self.knowledge >= 1000:
            print(f'{self.name} is ready to work!')
        self.is_ready = True


student = Student('Aktan', 'Bro')
student.learn_new_language('English', 60)
student.read_book('Harry Potter')
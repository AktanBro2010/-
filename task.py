# Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

# Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

# Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры как — experience и languages_frontend соответственно.

# Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.

# Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских классов.

# Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите их методы.

# Ввод должен быть:

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 
# Вывод:

# Python разработчик, уровень: Junior, потрачено 12 часов на программирование

# Javascript разработчик, уровень: Middle, потрачено 45 часов на программирование

# Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование 
class Coder:
    count_code_time = 0

    def get_info(self):
        ...

    def coding(self):
        ...

class Backend(Coder):
    def __init__(self, experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend

    def get_info(self):
        super().get_info()
        return f'Python разработчик, уровень: Junior, потрачено {self.count_code_time} часов на программирование'
    
    def coding(self, time):
        super().coding()
        self.count_code_time += time

class Frontend(Coder):
    def __init__(self, experience, languages_backend):
        self.experience = experience
        self.languages_backend = languages_backend

    def get_info(self):
        super().get_info()
        return f'Javascript разработчик, уровень: Middle, потрачено {self.count_code_time} часов на программирование'
    
    def coding(self, time):
        super().coding()
        self.count_code_time += time

class Fullstack(Backend, Frontend):
    def __init__(self, experience, languages_backend):
        super().__init__(experience, languages_backend)

    def get_info(self):
        super().get_info()
        return f'Python and JS разработчик, уровень: Senior, потрачено {self.count_code_time} часов на программирование'
    
    def coding(self, time):
        super().coding()
        self.count_code_time += time

a = Backend('ks', 'fd')
b = Frontend('fd', 'er')
c = Fullstack('df', 'fds')

a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 
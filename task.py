from datetime import datetime
class SmartPhones:
    def __init__(self, name, color, memory, battery = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery

    def str(self):
        return f'{self.name} {self.memory}'

    def charge(self, bat):
        self.battery += bat


class Iphone(SmartPhones):
    def __init__(self, name, color, memory, battery, ios: str):
        super().__init__(name, color, memory, battery)
        self.ios = ios

    def send_imessage(self, string):
        return f'sending {string} from {self.name} {self.memory}'


class Samsung(SmartPhones):
    def __init__(self, name, color, memory, battery, android: str):
        super().__init__(name, color, memory, battery)
        self.android = android

    def show_time(self):
        return datetime.now


phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 
print(phone.battery) 
phone.charge(20) 
print(phone.battery) 
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '1.17', '1.14.3') 
print(iphone7)
print(iphone7.send_imessage('hello'))
samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo', 'Oreo') 
print(samsung21.show_time())
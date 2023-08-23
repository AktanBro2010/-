class Person:
    def __init__(self, name, _phone_number, __card_number):
        self.name = name
        self._phone = _phone_number
        self.__card = __card_number


john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999")
print(john.name)
print(john._phone)
print(john._Person__card)
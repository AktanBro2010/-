class Person:
    def __init__(self, name, phone_number, card_number):
        self.name = name
        self._phone_number = phone_number
        self.__card_number = card_number

    def _validate_phone_number(self):
        if isinstance(self._phone_number, int) and str(self._phone_number)[0:3] == '996':
            pass
        else:
            self._phone_number = None

    def __validate_card_number(self):
        if isinstance(self.__card_number, int) and len(str(self.__card_number)) == 16:
            pass
        else:
            self.__card_number = None

    tolik = property(_validate_phone_number, __validate_card_number)

tolik = Person('Mike', 996706153343, 64732645732)
tolik.tolik
print(tolik.name)
print(tolik._phone_number)
print(tolik._Person__card_number)
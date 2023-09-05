class Person:
    def __init__(self, name, phone_number, card_number):
        self.name = name
        self._phone_number = self._validate_phone_number(phone_number)
        self.__card_number = self.__validate_card_number(card_number)
    
    def _validate_phone_number(self, phone_number):
        if type(phone_number) != (int, float):
            return None
        elif type(phone_number) == (int, float) and str(phone_number[0: 3]) == 996:
            self.__phone_number = phone_number

    def __validate_card_number(self, card_number):
        if type(card_number) != (int, float):
            return None
        elif type(card_number) == (int, float) and len(str(card_number)) == 16:
            self.__card_number = card_number

    @property
    def card(self):
        return self.__card_number

    @card.setter
    def card(self, phone):
        self.__card_number = phone

    

tolik = Person('Tolik', 996706153353, 9999999999999999)
print(tolik.name)
print(tolik._phone_number)
print(tolik.card)
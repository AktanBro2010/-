from views import *


class Phone(CreateMixin, ListingMixin, RetriveMixin, UpdateMixin, DeleteMixin):
    def get_start(self):
        choice = input('Привет\nНачнем? Да/Нет ')
        while choice.lower() == 'Да':
            print('Что вы хотите сделать?\n1 - добавить товар,\n2 - просмотреть список товаров,\n3 - просмотреть один товар,\n4 - изменить товар,\n5 - удалить товар')
            choice1 = input('Выберите действие: ')
            if choice1 == '1':
                super().create()
            elif choice1 == '2':
                super().listening()
            elif choice1 == '3':
                super().retrive()
            elif choice1 == '4':
                super().update()
            elif choice1 == '5':
                super().delete()
            else:
                print('Такого действия нет!')
    
obj = Phone()
obj.get_start()

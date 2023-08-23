import json


FILE = 'data.json'


class GetMixin:
    def get_data(self):
        try:
            with open(FILE) as file:
                return json.load(file)
        except:
            with open(FILE, 'w') as file:
                data = []
                json.dump(data, file)
                return data
        

    def get_id(self):
        with open('id.txt') as file:
            id = int(file.read())
            id += 1
            
        with open('id.txt', 'w') as file:
            file.write(str(id))

        return id
    

class CreateMixin(GetMixin):
    def create(self):
        data = super().get_data()

        try:
            new_product = {
                'id': super().get_id(),
                'model': input('Введите модель телефона: '),
                'price': int(input('Введите стоимость телефона: ')),
                'color': input('Введите цвет товара: '),
                'storage': int(input('Введите память телефона: '))
            }
        except ValueError:
            print('Введите корректные данные!')
            self.create()
        
        else:
            data.append(new_product)
            print(data)
            with open(FILE, 'w') as file:
                json.dump(data, file)
            return 'Successfully created!'


class ListingMixin(GetMixin):
    def listening(self):
        print('Список телефонов')
        data = super().get_data()
        print(data)

        
class RetriveMixin(GetMixin):
    def retrive(self):
        data = super().get_data()
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('id должно быть числом!') 
            self.retrive()

        else:
            one_product = list(filter(lambda x: x['id'] == id ,data))
            if not one_product:
                print('Такого продукта нет')
            else:
                print(one_product[0])


class UpdateMixin(GetMixin):
    def update(self):
        data = super().get_data()

        try:
            id = int(input('Введите id телефона'))
        except ValueError:
            print('id должно быть числом')
            self.update()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product:
                print('Такого товара нет')
                
            else:
                product_index = data.index(one_product[0])
                try:
                    choice = int(input('Что вы хотите изменить? 1 - model, 2 - price, 3 - color, 4 - color'))
                except ValueError:
                    print('Введите число!')
                    choice = int(input('Что вы хотите изменить? 1 - model, 2 - price, 3 - color, 4 - color'))

                if choice == 1:
                    data[product_index]['model'] == input('Введите новую модель: ')
                    flag = True

                elif choice == 2:
                    data[product_index]['price'] == int(input('Введите новую стоимость: '))
                    flag = True

                elif choice == 3:
                    data[product_index]['color'] == input('Введите новый цвет: ')
                    flag = True

                elif choice == 4:
                    data[product_index]['storage'] == int(input('Введите новую память: '))
                    flag = True

                else:
                    print('Такого поля нет!')

                with open(FILE, 'w') as file:
                    json.dump(data, file)
            if flag:
                print('Объект успешно изменён')
            else:
                print('Такого товара нет')
            

class DeleteMixin(GetMixin):
    def delete(self):
        data = super().get_data()

        try:
            id = int(input('Введите id товара: '))
        except ValueError:
            print('Такого id нет')
            self.delete()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
            
            if not one_product:
                print('Такого товара нет!')
            else:
                index = data.index(one_product[0])

                data.pop(index)
                with open(FILE, 'w') as file:
                    json.dump(data, file)
                print('Товар успешно удален')



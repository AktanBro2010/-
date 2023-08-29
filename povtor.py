# Николай – оригинальный человек. 
# Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился. 
# Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”. 
# В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
# Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).

# class Nikola:
#     __slots__ = ['name', 'age']
#     def __init__(self, name, age):
#         self.name = name = 'Николай'
#         self.age = age

# nikolai = Nikola('Ni', 12)
# print(nikolai.name)


# '''Герой.
# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты(Solder) и герои(Hero).
# У всех есть свойство, содержащее уникальный номер объекта(id), и свойство в котором хранится принадлежность команде(team).
# У солдат есть статический метод "go_hero", который в качестве параметра принимает уникальный номер(id) героя. И возвращает 'Иду за героем {уникальный номер героя}'
# У героев есть атрибут класса 'level = 0' и есть метод увеличения собственного уровня 'level_up' который при вызове увеличивает уровень героя на единицу.
# В основной ветке программы создается по одному герою 'hero1' и 'hero2'.
#     hero1 = (1, 'Blue)
#     hero2 = (2, 'Red)
# В цикле генерируются объекты-солдаты(10 солдат). В списке obj1 будут храниться обьекты солдаты команды 'Blue', а в obj2 'Red'. Их принадлежность команде определяется случайно.
# Измеряется длина списков солдат противоборствующих команд и выводится на экран сообщение. Если количество солдат команды Blue больше команды Red, тогда выведете сообщение "Первый герой победил у него: {len(obj1)} солдат", если же количество солдат второй команды больше: "Второй герой победил у него: {len(obj2)} солдат" иначе "Количество солдат одинаковое!".
# Также у героя, принадлежащего команде с более длинным списком, поднимается уровень.
# Отправьте одного из солдат первого героя следовать за ним. Также вывидите уровень героев.


# class Soldier:
#     def __init__(self, id_, team):
#         self.id_ = id_
#         self.team = team

#     def go_hero(self, id):
#         return f'Иду за героем {id}'


# class Hero:
#     def __init__(self, id, team, level=0):
#         self.id = id
#         self.team = team
#         self.level = level
    
#     def level_up(self):
#         self.level += 1


# hero1 = (1, 'Blue')
# hero2 = (2, 'Red')
# obj1 = []
# obj2 = []

# import random

# for i in range(10):
#     res = random.choice(['Blue', 'Red'])
#     print(res)
#     if res == 'Red':
#         obj2.append(Soldier(random.randint(1, 1000), res))
#     else:
#         obj1.append(Soldier(random.randint(1, 1000), res))

# if len(obj1) > len(obj2):
#     hero1.level_up()
#     print(f'Второй герой победил')


import json

FILE = 'user.json'

class RegisterMixin:

    def validate_password(self, password: str, password_confirm):
        if password != password_confirm:
            raise ValueError(
                'Пароли не совпадают'
            )
        elif len(password) < 8:
            raise ValueError(
                'пароль слишком короткий'
            )
        elif password.isdigit() or password.isalpha():
            raise ValueError(
                'Пароль должен состоять тз букв и цифр!'
            )



    def register(self, username, password, password_confirm):
        self.validate_password(password, password_confirm)

        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
                # print(data)
            except:
                id = 1
                data = []

        with open(FILE, 'w') as file:
            if data:
                is_username_used = any([x['username']==username for x in data])
                if is_username_used:
                        # json.dump(data, file)
                    raise ValueError('Такой username уже существует')
                else:
                    
                    data.append({'id': id, 'username': username, 'password': password})
                    json.dump(data, file)
                    print('Аккаунт успешно создан')
            else:
                    data.append({'id': id, 'username': username, 'password': password})
                    json.dump(data, file)
                    print('Аккаунт успешно создан')


class LoginMixin:

    def login(self, username, password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any([x['username'] == username for x in data])
            if not is_registered:
                raise Exception('Пользователь не найден, пройдите регистрацию!')
            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            print(user_data)
            if user_data['password'] != password:
                raise Exception('Неверный пароль')
            print('Вы успешно вошли в свой аккаунт')
                

class ChangePasswordMixin:
    def change_password(self, username, old_password, new_password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registered = any([x['username'] == username for x in data])
            if not is_registered:
                raise Exception('Пользователь не найден, пройдите регистрацию!')
            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            print(user_data)
            if user_data['password'] != old_password:
                raise Exception('Неверный пароль')
            print('Вы успешно вошли в свой аккаунт')
            data.remove(user_data)
            user_data['password'] = new_password
            data.append(user_data)
            with open(FILE, 'w') as file:
                json.dump(data, file)
            print('Пароль успешно изменен')


class User(RegisterMixin, LoginMixin, ChangePasswordMixin):
    pass

user1 = User()
# user1.register('test2', '1234567k', '1234567k')
user1.change_password('test3', '1234567k', 'superpassword')
# class Car:
#     def __init__(self, model):
#         self.__model = model

#     @property
#     def get_model(self):
#         print(self.__model)
    


#     model = property(lambda self: self.__model)

# car = Car('BMW')
# print(car.model)


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        print('getter')
        return self.__radius
    
    def set_radius(self, value):
        print('setter')
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError('Invalid value, must be int or float object')
        else:
            self.__radius = value

    def del_radius(self):
        print('deletter')
        del self.__radius

    radius = property(get_radius, set_radius, del_radius, doc='The private radius property')


# circle = Circle(5)
# print(circle.radius)
# circle.radius = 0
# del circle.radius


class PrivateProject:
    __github_link = 'https://github.com/AktanBro2010/telegram_bot_30_ev'
    __developers = ['Aktan', 'John Pork', 'DJ Khaled']

    def __init__(self, username):
        self.user = username

    @property
    def project(self):
        if self.user in self.__developers:
            print(f'There is a link for private project: {self.__github_link}')
        else:
            print('Forbidden')

    userbek = property(project,)


# user = PrivateProject('John Pork')
# user.project


class ValidateMixin:
    def validate_password(self, password):
        if password.isdigit() or password.isalpha():
            raise Exception(
                'Password must contain numbers and integers'
            )
        if len(password) < 4:
            raise Exception(
                'Too short password, at least 4 symbols'
            )
        return password
    
    def validate_email(self, email):
        if not '@' in email:
            raise Exception(
                'It is not email'
            )
        return email


class User(ValidateMixin):
    def _create_user(self, email, password):
        self.email = self.validate_email(email)
        self.__password = self.validate_password(password)

    def create_user(self, email, password):
        self.is_superuser = False
        self._create_user(email, password)

    def create_superuser(self, email, password):
        self.is_superuser = True
        self._create_user(email, password)


    def admin_login(self, password):
        if self.is_superuser == True:
            if password == self.__password:
                print('Succesfully logged in')
            else:
                print('Invalid password')
        else:
            print('Forbidden')


user1 = User()
user2 = User()

# user1.create_superuser('user1@mail.ru', 'sdfpo2')
# user2.create_user('user2@gmail.com', 'superpassword2')
# print(user1._User__password)
# user1.admin_login('sdfpo2')
# user2.admin_login('superpassword2')


class CoordinateError(Exception):
    pass
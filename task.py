class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):
        if len(self.password) < 8 and len(self.password) > 14:
            print('Password should be longer than 8, and less than 15')
        elif self.password.isdigit() == False:
            print('Password should contain numbers too')
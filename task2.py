class Math:
    def __init__(self, number):
        self.number = number
    
    def get_factorial(self):
        factorial = 1
        for i in range(2, self.number+1):
            factorial *= i
        return factorial

    def get_sum(self):
        factorial = 1
        for i in range(2, self.number+1):
            factorial += i
            return factorial
        
    def get_mul_table(self):
        for i in range(1, 10):
            return f'{self.number}x{i}={self.number * i}'
        

math = Math(12)
print(math.get_mul_table())
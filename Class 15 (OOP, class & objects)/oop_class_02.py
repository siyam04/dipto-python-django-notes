########################################## Constructor ########################################


class Robot:

    def __init__(self, name):
        self.name = name

########################################## Constructor ########################################


class Calculator:

    def __init__(self, a, b):  # This __init__() method is constructor.
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        try:
            return self.a / self.b

        except ZeroDivisionError:
            return "It's impossible to divide by Zero!"

# Body


my_calculator = Calculator(45, 3)  # Only two values because we pass to constructor only a, b.

result = my_calculator.add()
print(result)

result = my_calculator.sub()
print(result)

result = my_calculator.mul()
print(result)

result = my_calculator.div()
print(result)


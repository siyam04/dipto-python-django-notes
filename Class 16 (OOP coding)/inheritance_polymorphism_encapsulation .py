
########################################## Inheritance ########################################


# Parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

# Body


peggy = Penguin()

peggy.whoisThis()
peggy.swim()
peggy.run()

"""
Output:
------------------
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
------------------

In the above program, we created two classes i.e. Bird (parent class) and Penguin (child class). 
The child class inherits the functions of parent class. We can see this from swim() method. 
Again, the child class modified the behavior of parent class. We can see this from whoisThis() method. 
Furthermore, we extend the functions of parent class, by creating a new run() method.
Additionally, we use super() function before __init__() method. 
This is because we want to pull the content of __init__() method from the parent class into the 
child class.

"""


########################################## Encapsulation ########################################


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

# Body


c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

"""
Output:
--------------------
Selling Price: 900
Selling Price: 900
Selling Price: 1000
--------------------

In the above program, we defined a class Computer. We use __init__() method to store the maximum 
selling price of computer. We tried to modify the price. However, we can’t change it because 
Python treats the __maxprice as private attributes. To change the value, we used a setter 
function i.e setMaxPrice() which takes price as parameter.

"""


########################################## Polymorphism ########################################


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)

"""
Output:
------------------
Parrot can fly
Penguin can't fly
------------------

In the above program, we defined two classes Parrot and Penguin. Each of them have common method 
fly() method. However, their functions are different. To allow polymorphism, we created common 
interface i.e flying_test() function that can take any object. Then, we passed the objects 
blu and peggy in the flying_test() function, it ran effectively.

"""


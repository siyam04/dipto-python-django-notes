# class Robot:
#     name = 'wall-e'
#
# # Body
#
# robot = Robot()
#
# r1_name = robot.name
# print(r1_name)


##################################################################################


# class Robot:
#     name = 'wall-e'
#
#     def say_hello(self):
#         return 'HI, Hello!'
#
#
# robot = Robot()
#
# print(robot.name)
#
# print(robot.say_hello())

##################################################################################
#
#
# class Robot:
#     name = 'wall-e'
#
#     def say(self, something):
#         return str(something)
#
#
# robot = Robot()
#
# print(robot.name)
#
# print(robot.say('Bangladesh'))
#
# print(robot.say('Dhaka'))

##################################################################################


# class level variable and instance level variable

class Robot:
    company = 'BNL'

    def __init__(self, name):
        self.name = name


robot1 = Robot('wall-e')
robot2 = Robot('eve')

result1 = robot1.company
print(result1)

result2 = robot2.company
print(result2)

result3 = robot1.name
print(result3)

result3 = robot2.name
print(result3)

compare = robot1.company is robot2.company
print(compare)

class_variable = Robot.company
print(class_variable)





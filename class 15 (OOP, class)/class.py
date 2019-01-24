## importing module

import this
import random
from random import randint

import math

math.pi
from math import pi

pi
from math import *

pi
sqrt
from math import pi, sqrt


## classes

class Robot:
    name = 'wall-e'

## objects

class Robot:
    name = 'wall-e'

robot1 = Robot()
robot2 = Robot()

robot1 is robot2
False

robot1.name
'wall-e'
robot2.name
'wall-e'

## method

class Robot:
    name = 'wall-e'

    def say_hello(self):
        return 'HI, Hello!'


robot = Robot()
robot.name
'wall-e'
robot.say_hello()
'HI, Hello!'


class Robot:
    name = 'wall-e'

    def say(self, somthing):
        return str(somthing)


robot = Robot()
robot.name
'wall-e'
robot.say('bangladesh')
'bangladesh'
robot.say('dhaka')
'dhaka'

## __init__()

class Robot:
    def __init__(self, name):
        self.name = name


robot1 = Robot('wall-e')
robot2 = Robot('eve')

robot1 is robot2
False

robot1.name
'wall-e'
robot2.name
'eve'

## class level variable and instance level variable

class Robot:
    company = 'BNL'

    def __init__(self, name):
        self.name = name


robot1 = Robot('wall-e')
robot2 = Robot('eve')

robot1.company
'BNL'
robot1.name
'wall-e'

robot2.company
'BNL'
robot2.name
'eve'

robot1.company is robot2.company
True
Robot.company
'BNL'
Robot.name
'AttrubuteError'
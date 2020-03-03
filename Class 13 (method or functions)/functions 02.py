############################################## args ####################################


def add(*args):

    print(type(args))

    temp = 0

    for i in args:
        temp = temp + i

    return temp

# Body


result = add(1, 2, 22, 12, 17, 21, 98)

print(result)

############################################## kwargs ####################################


def add(**kwargs):

    print(type(kwargs))

    temp = 0

    for key in kwargs:
        temp = temp + kwargs[key]

    return temp

# Body


result = add(a=1, b=2, c=3, d=4)

print(result)


############################################## Rucursion ####################################


def factorial(number):

    if number == 0:
        return 1
    else:
        return number * factorial(number-1)

# Body


value = int(input('Enter a Number:\n'))

print('Factorial of', value, 'is: ', factorial(value))


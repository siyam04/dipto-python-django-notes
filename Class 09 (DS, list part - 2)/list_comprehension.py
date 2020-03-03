# Syntax of List Comprehension
# [expression for item in list]

#################################################################

# Iterating through a string Using for Loop
data = []

for letter in 'human':
    data.append(letter)

print('Normal List Data:', data)

######################### Same code using List Comprehension ########################

# Iterating through a string Using List Comprehension
data = [letter for letter in 'human']
print('List Comprehension:', data)

#################################################################

# Using if with List Comprehension
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

#################################################################

# Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

#################################################################

# if...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)



#
# input1 = int(input('Enter a number: \n'))
# input2 = int(input('Enter another number: \n'))
#
# for i in range(input1, input2):
#     print(i)
#
# #################################################################
#
# input3 = int(input('Enter a number: \n'))
#
# for i in range(0, input3):
#     print(i)
#
# #################################################################
#
# L = []
#
# input1 = int(input('Enter a number: \n'))
# input2 = int(input('Enter another number: \n'))
#
# for i in range(input1, input2):
#     L.append(i)
#
# print(L)

#################################################################
from pprint import pprint

L = [1, 2, 3, 4, 5]
N = []

for i in L:
    print(i, end='')
    N.append(i)

print('\n', N[1])


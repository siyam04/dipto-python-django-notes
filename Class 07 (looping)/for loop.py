input1 = int(input('Enter a number: \n'))
input2 = int(input('Enter another number: \n'))

for i in range(input1, input2):
    print(i)

#################################################################

input3 = int(input('Enter a number: \n'))

for i in range(0, input3):
    print(i)

#################################################################

L = []

input1 = int(input('Enter a number: \n'))
input2 = int(input('Enter another number: \n'))

for i in range(input1, input2):
    L.append(i)

print(L)

#################################################################

L = [1, 2, 3, 4, 5]
casted =(L)

for i in L:
    print(i)

#################################################################

dic = {1: 'Siyam', 2: 'Dipto', 3: 'Barna'}
for K, V in dic.items():
    print('{}: {}'.format(K, V))

#################################################################

dic = {1: 'Siyam', 2: 'Dipto', 3: 'Barna'}

for Keys, Values in dic.items():
    print('{', Keys, ':', Values, '}')

#################################################################



dic = {'key1': '777777777777', 'key2': '9999999999999999999999999999999999999999.9'}
print(dic, '\n', type(dic))
print(dic["key1"])
print(dic["key2"])

d = {1: 100, 2: 500}

########################################################################

dic = {'Dhaka': 10, 'Bogra': 20}
print(dic)
dic['Dhaka'] = 100
print(dic)

################################################################

dic = {1: 'Python', 2: 'Django', 3: 'JavaScript'}

for K, V in dic.items():
    print('{}: {}'.format(K, V))

################################################################

dic = {1: 'Python', 2: 'Django', 3: 'JavaScript'}

for Keys, Values in dic.items():
    print('{', Keys, ':', Values, '}')







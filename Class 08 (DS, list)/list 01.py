
Li = []
print(type(Li))

###################################################################

Li = ['smart', 22, 50.55]

print(type(Li[0]))
print(type(Li[1]))
print(type(Li[2]))

####################################################################

Li_1 = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(Li_1[0:3])
print(Li_1[3:6])
print(Li_1[5])
print(Li_1[-2])

####################################################################

Li_2 = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(Li_2[0:6:2])
print(Li_2[0:6:3])

###################################################################

Li_3 = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(Li_3[::-1])
print(Li_3[::1])

add = Li_3[0] + '_boy'
print(add)

print(len(Li_3))

###################################################################

Li_4 = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(type(Li_4))

rm = Li_4.remove('smart')
print(rm)

print(Li_4)


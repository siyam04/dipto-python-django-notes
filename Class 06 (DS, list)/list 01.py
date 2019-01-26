dipto = []
print(type(dipto))

dipto = ['smart', 22, 50.55]

print(type(dipto[0]))
print(type(dipto[1]))
print(type(dipto[2]))

print(dipto)

print(len(dipto))

print(dipto[-1])
print(dipto[-2])
print(dipto[-3])

dipto = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(dipto[0 : 3])
print(dipto[3 : 6])
print(dipto[-1 : 1])

print(dipto[0 : 6 : 2])
print(dipto[0 : 6 : 2])
print(dipto[2 : 5 : 2])

print(dipto[::1])

add = dipto[0] + '_boy'

print(add)
print(dipto)

dipto = ['smart', 22, 50.55, 'Pythonaista', 100, 'sun-glass']

print(type(dipto))

rm = dipto.remove('smart')
print(rm)

# append()

li = [1, 2, 3, 4, 5, 6]
li.append(7)
print(li)

################################################################

# insert()

li2 = [1, 2, 3, 4, 5, 6]
li2.insert(0, 'Element')
print(li2)

################################################################

# remove()

li3 = [1, 2, 3, 4, 5, 6, 'new']
li3.remove('new')
print(li3)

################################################################

# sort()

li4 = [10, 5, 1, 20, 3, 4, 5, 8]
li4.sort()
print(li4)

################################################################

# reverse()

li5 = [1, 2, 3, 4, 5]
li5.reverse()
print(li5)

################################################################

# extend()

li6 = [1, 2, 3, 4, 5]
li6.extend(['New', 6, 7, 8, 9, 10])
print(li6)

################################################################

# extend()

li6 = [1, 2, 3, 4, 5]
li6.extend(['New', 6, 7, 8, 9, 10])
print(len(li6))
print(li6)

################################################################

# range()

for i in range(1, 11):
    print(i, '\n')

################################################################

# count()

li2 = [1, 2, 3, 4, 5, 3, 3]
print(li2.count(3))

################################################################



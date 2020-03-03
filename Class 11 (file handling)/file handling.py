# File Read

my_file = open('test.txt', 'r')
print(my_file.read())
my_file.close()

my_file_2 = open('C:\\Users\\SSD-Siyam\\Desktop\\new.txt', 'r') # This line is for Path
print(my_file_2.read())
my_file_2.close()

random = open('C:\\Users\\SSD-Siyam\\Desktop\\random.txt', 'r')
new = random.read()
print(new)
random.close()
content = my_file.read()
print(content)
my_file.close()

################################################################

# File Write

my_file = open('test_write.txt', 'w')
my_file_2 = open('C:\\Users\\SSD-Siyam\\Desktop\\test.txt', 'r') # This line is for Path
content = my_file.write('I love Python!\nPython is a Open Source Language.')
print(content)
my_file.close()

################################################################

# File Append

my_file = open('test_write.txt', 'a')
content = my_file.write('\nI also like Django!')
print(content)
my_file.close()

################################################################

# File Operations

my_file = open('test_write.txt', 'r')
content = my_file.read(5)
print(content)


# Pointer's position finding

position = my_file.tell()
print(position)

# Pointer starts from beginning

print(my_file.seek(0, 0))

# Again total content
content = my_file.read()
print(content)

# File closing
my_file.close()


# if we use 'with', then no need to closing File

with open('test_write.txt', 'r') as my_file_2:
    content = my_file_2.read()
    print(content)


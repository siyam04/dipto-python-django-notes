## File Read
my_file = open('test.txt', 'r')
my_file_2 = open('C:\\Users\\SSD-Siyam\\Desktop\\test.txt', 'r') # This line is for Path
content = my_file.read()
print(content)
my_file.close()


## File Write
my_file = open('test_write.txt', 'w')
# my_file_2 = open('C:\\Users\\SSD-Siyam\\Desktop\\test.txt', 'r') # This line is for Path
content = my_file.write('Dipto is very Lazy!')
print(content)
my_file.close()


## File Append
my_file = open('test_write.txt', 'a')
content = my_file.write('\nDipto has a Girlfriend!')
print(content)
my_file.close()


## File Operations
my_file = open('test.txt', 'r')
# 1
content = my_file.read(5)
print(content)
# 2
content = my_file.read()
print(content)
# Pointer's position finding
position = my_file.tell()
print(position)
# Pointer starts from beginning
my_file.seek(0, 0)
# Again total content
content = my_file.read()
print(content)
# File closing
my_file.close()


## if we use 'with', then no need to closing File
with open('test.txt', 'r') as my_file:
    content = my_file.read()
    print(content)


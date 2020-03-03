## basic
# 1

x = 1

try:
  print(x)

except:
  print("An exception occurred!")

################################################################

# 2

x = 2

try:
  print(x)

except NameError:
  print("Variable x is not defined")

except:
  print("Something else went wrong")

################################################################

# 3

try:
    1 / 0

except:
    print("You cannot divide by zero!")

################################################################

4

try:
    1 / 0

except ZeroDivisionError:
    print("You cannot divide by zero!")

################################################################

## Try, Except, Else

try:
  print("Hello")

except:
  print("Something went wrong")

else:
  print("Nothing went wrong")

################################################################

## Try, Except, Finally
# 1

x = 1

try:
  print(x)

except:
  print("Something went wrong")

finally:
  print("The 'try except' is finished")

################################################################

# 2

try:
  # f = open("test.txt")
  f = open("test.txt", 'w')
  f.write("This is a sentence.")
  # f.read()

except:
  print("Something went wrong when writing to the file")

finally:
  f.close()

################################################################

## Using Dictionary

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
    print(value)

except IndexError:
    print("This index does not exist!")

except KeyError:
    print("This key is not in the dictionary!")

except:
    print("Some other error occurred!")


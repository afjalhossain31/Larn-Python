num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print(num1 + num2)

# Python automatically converts
# a to int
a = 7
print(type(a))

# b to float
b = 3.0
print(type(b))

# c to float as it is a float addition
c = a + b
print(c)
print(type(c))

# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

num3 = 20
num4 = 20.5
print(num3 + num4)
print(num3 * num4)

a = 11
f = float(a)
print(f)
b = hex(a)
print(b)
c = oct(a)
print(c)
d = bin(a)
print(d)
char = "A"
e = ord(char)
print(e)
e = 65
char = chr(e)
print(char)

# creating and accessing a tuple
my_tuple = (10, 20, 30, 40)

# Accessing elements in a tuple
first_element = my_tuple[0]
last_element = my_tuple[-1]

print(first_element)
print(last_element)

# Update the list
my_tuple = (1, 2, 3)

my_list = list(my_tuple)
my_list[1] = 10

my_tuple = tuple(my_list)
print(my_tuple)

# unpack
# Tuple
my_tuple = (1, 2, 3)
# Unpack tuple
a, b, c = my_tuple
print(a, b, c)

# Loop

my_tuple = (1, 2, 3)

# Loop over tuple
for item in my_tuple:
    print(item)

# Join

my_tuple = ("a", "b", "c")

# Join tuple elements into a string
joined_string = "".join(my_tuple)
print(joined_string)
# Tuple Method

my_tuple = (1, 2, 3, 1, 1)

# Use count() method
count_of_ones = my_tuple.count(1)
print(count_of_ones)

# Using array Module
import array as arr

my_array = arr.array("i", [1, 2, 3, 4, 5, 6, 7])

print(my_array)
my_array.append(6)
print(my_array)
my_array.insert(2, 10)
print(my_array)
my_array.pop(1)
print(my_array)
my_array.reverse()
print(my_array)


first_element = my_array[0]
print(first_element)
last_element = my_array[-1]
print(last_element)
slice_of_array = my_array[1:3]
print(slice_of_array)


length = len(my_array)
print(length)
min_value = min(my_array)
print(min_value)
max_value = max(my_array)
print(max_value)
sum_of_elements = sum(my_array)
print(sum_of_elements)

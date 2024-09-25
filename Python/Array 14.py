# Using Lists
array = [1, 2, 3, 4, 5]

array.append(6)  # Add element
print(array)
array.insert(2, 10)  # Insert specific index
print(array)
array.remove(3)  # Remove first element
print(array)
array.pop(1)  # Remove element
print(array)


array.reverse()  # Reverse the list
print(array)
array.sort()  # Sort the list
print(array)
sorted_arr = sorted(array)  # returns a new list
print(sorted_arr)

first_element = array[0]
print(first_element)
last_element = array[-1]
print(last_element)
slice_of_array = array[1:3]
print(slice_of_array)

length = len(array)  # Get length of the list
print(length)
min_value = min(array)  # Get minimum value
print(min_value)
max_value = max(array)  # Get maximum
print(max_value)
sum_of_elements = sum(array)
print(sum_of_elements)

squares = [x**2 for x in array]
print(squares)

# Clear the list at the end if needed
array.clear()  # Remove all

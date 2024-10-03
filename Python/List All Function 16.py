# 1. append() Function
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# 2. Extend() function
fruits = ["apple", "banana"]
more_fruits = ["orange", "orange"]
fruits.extend(more_fruits)
print(fruits)

# 3.insert() function
fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "orange")
print(fruits)

# 4.remove() function
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")
print(fruits)

# 5.pop() function
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
print(fruits)

# 6. clear() function
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)

# 7. index() function
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")
print(index)

# 8.count() function
fruits = ["apple", "banana", "cherry", "banana"]
count = fruits.count("banana")
print(count)

# 9.sort() function
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

# 10.reverse() function
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)


# 11.list() function
string = "hello"
letters = list(string)
print(letters)

# 12.max()
numbers = [1, 2, 3, 4, 5, 64, 34, 234]
max_value = max(numbers)
print(max_value)

# 13. min() function
numbers = [1, 2, 3, 4]
min_value = min(numbers)
print(min_value)

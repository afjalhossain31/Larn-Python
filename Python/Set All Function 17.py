# add() add element to the set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# 2.update()
fruits = {"apple", "banana"}
more_fruits = ["cherry", "orange"]
fruits.update(more_fruits)  # extend
print(fruits)

# 3.discard()
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
fruits.discard("pear")
print(fruits)

# 4.Union()
set1 = {"apple", "banana"}
set2 = {"cherry", "banana"}
result = set1.union(set2)
print(result)

# 5.intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "orange"}
result = set1.intersection(set2)
print(result)

# 6. difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "orange"}
result = set1.difference(set2)
print(result)

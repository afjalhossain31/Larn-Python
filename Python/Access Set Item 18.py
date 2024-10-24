my_set = {"apple", "banana", "cherry"}

for item in my_set:
    print(item)
# Check if an item exists
if "banana" in my_set:
    print("Banana is in the set")
my_list = list(my_set)

print("First item:", my_list[0])

first_item = next(iter(my_set))

print("First item using iter():", first_item)

# abdullah al afjal

student = {"name": "Abdullah", "subject": {"phy": 95, "chem": 89, "math": 89}}

# Key function return all keys
print(len(list(student.keys())))

# Value function returns all values

print(student.values())
print(list(student.values()))

# items method

print(student.items())

# get ( ) function
print(student["name"])
print(student.get("name"))
# update( newdict) insert the specified item
new_dict = {"City": "Dhaka", "age": 13}
student.update(new_dict)
print(student.update({"City": "Dhaka"}))
print(student)

words = ["Hello", "world", "Python", "is", "awesome"]
sentence = " ".join(words)
print("Example 1-Joining words with spaces:\n", sentence)


fruits = ["apple", "banana", "cherry"]
fruits_string = ", ".join(fruits)
print("\nExample 2 -Joining fruits with commas:\n", fruits_string)


tuple_of_words = ("join", "method", "in", "Python")
result_with_hyphen = "-".join(tuple_of_words)
print("\nExample 3 -Joining tuple of words with hyphen:\n", result_with_hyphen)


chars = ["P", "y", "t", "h", "o", "n"]
joined_chars = "".join(chars)
print("\nExample 4 -Joining characters into a string:\n", joined_chars)


lines = ["Line 1", "Line 2", "Line 3"]
joined_lines = "\n".join(lines)
print("\nExample 5 -Joining lines with newline characters:\n", joined_lines)


numbers = [1, 2, 3, 4]
numbers_string = ", ".join(map(str, numbers))
print("\nExample 6 -Joining numbers after converting to strings:\n", numbers_string)


special_join = " | ".join(["apple", "orange", "grape"])
print("\nExample 7 -Joining with special characters:\n", special_join)

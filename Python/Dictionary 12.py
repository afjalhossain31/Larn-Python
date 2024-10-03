dict = {
    "name": "Daffodil",
    "subject": ["python", "C++", "java"],
    "Topics": ("dict", "set"),
    "age": 23,
    "is_adult": True,
    "marks": 90.2,
}
# Null dictionary
null_dict = {}

print(null_dict)

print(type(dict))
print(dict["name"])
print(dict["subject"])
print("\n\n\n\n\n\n")


def top_student(student_scores):
    # Comprehension : {key: value for key, value in iterable}
    student_dict = {name: score for name, score in student_scores}
    # {'Alice': 85, 'Bob': 90, 'Charlie': 78}
    top_student = max(student_dict, key=student_dict.get)

    return (
        student_dict,
        f"Top Student: {top_student} with {student_dict[top_student]} marks",
    )


student_scores = [("Alice", 85), ("Bob", 90), ("Charlie", 80)]

student_data, top_student = top_student(student_scores)

print(student_data)
print(top_student)

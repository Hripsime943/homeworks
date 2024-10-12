class_students = {
    "student1": {"name": "Alice", "age": 20, "grade": 85},
    "student2": {"name": "Bob", "age": 22, "grade": 92},
    "student3": {"name": "Charlie", "age": 19, "grade": 78},
    "student4": {"name": "Diana", "age": 21, "grade": 90}
}
specific_student = input("please write student's name: ")
age = class_students[specific_student]['age']
print(f"The age of student is {age}.")
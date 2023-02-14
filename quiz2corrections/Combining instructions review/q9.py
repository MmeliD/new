def display_student(name, age):
    print(name, age)

showStudent = display_student
name = input("Enter name:")
age = int(input(""))

showStudent(name, age)
# process with unlimited before you write stop 

students = []

print("end this proses to write stop ")

while (name := input("name or and: ")) != 'stop':
    roll = int(input("roll: "))
    marks = int(input("marks: "))
    students.append({"name": name, "roll": roll, "marks": marks})


students = sorted(students, key=lambda x: x['roll'])

print("\nRoll\tName\tMarks")
for student in students:
    print(f"{student['roll']}\t{student['name']}\t{student['marks']}")


# process with your entered limit


students = []
n_s = int(input("Enter the number of student: "))
for _ in range(n_s):
    name = input("Enter the student name: ")
    roll = int(input("Enter the student roll: "))
    marks =int(input("Enter the student marks: "))
    students.append({'name':name,'roll':roll,'marks':marks})
print("Roll\tName\tMarks")
for student in students:
    print(f"{student['roll']}\t{student['name']}\t{student['marks']}")


# process with code write 


students = [
    {"name": "Alice", "roll": 1, "marks": 85},
    {"name": "Bob", "roll": 2, "marks": 78},
    {"name": "Charlie", "roll": 3, "marks": 92},
    {"name": "David", "roll": 4, "marks": 67},
    {"name": "Eva", "roll": 5, "marks": 88}
]
print("Roll\tName\tMarks")
for student in students:
    print(f"{student['roll']}\t{student['name']}\t{student['marks']}")
from clases.clases import Student

students_data = [
    {"name": "Tomas", "age": 20, "grades": [4.0, 3.7, 4.8]},
    {"name": "Pablo", "age": 22, "grades": [2.5, 3.6, 2.7]},
    {"name": "Samuel", "age": 21, "grades": [1.5, 4.1, 5.0]},
]

students: list[Student] = []

for register in students_data:
    student = Student(register["name"], register["age"], register["grades"])
    students.append(student)

threshold = 3

for st in students:
    print(st)

filtered_students: list[Student] = []
for st in students:
    if st.average_grade() >= threshold:
        filtered_students.append(st)

dict_students: dict[str, Student] = {}
for st in students:
    if st.average_grade() >= threshold:
        dict_students[st.name] = st

print(f"Diccionario de estudiantes")
print(dict_students)

print(f"Students with average grade over {threshold}")
for st in filtered_students:
    print(st)

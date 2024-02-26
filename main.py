from clases.clases import Student

n = int(input("Ingrese una nota"))
s: Student = Student("Tomas", 18, [])

Student.add_grade(n)

print(s)

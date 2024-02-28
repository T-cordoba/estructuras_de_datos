class Student:
    def __init__(self,  name: str, age: int, grades: list[float]):
        self.name: str = name
        self.age: int = age
        self.grades: list[float] = grades

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

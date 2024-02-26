class Student:
    def __init__(self,  name: str, age: int, grades: list):
        self.name: str = name
        self.age: int = age
        self.grades: list = grades

    def add_grade(self, n: int):
        self.grades = self.grades.append(n)
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grades(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            raise ValueError("Grade must be between 0 and 100")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades.values()) / len(self.grades)
        return 0

class StudentTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number not in self.students:
            self.students[roll_number] = Student(name, roll_number)

    def add_grades(self, roll_number, grades):
        if roll_number in self.students:
            for subject, grade in grades.items():
                self.students[roll_number].add_grades(subject, grade)

    def get_student(self, roll_number):
        return self.students.get(roll_number)

    def calculate_average(self, roll_number):
        student = self.get_student(roll_number)
        if student:
            return student.calculate_average()
        return 0

class Student:
    def __init__(self, student_id, student_name, student_CGPA):
        self.student_id = student_id
        self.student_name = student_name
        self.student_CGPA = student_CGPA

    def display_student(self):
        return f"Name: {self.student_name}\nID: {self.student_id}\nCGPA: {self.student_CGPA}\n"


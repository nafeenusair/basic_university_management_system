class Faculty:
    def __init__(self, faculty_id, faculty_name, faculty_position):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.faculty_position = faculty_position

    def display_faculty(self):
        return f"Name: {self.faculty_name}\nID: {self.faculty_id}\nPosition: {self.faculty_position}\n"

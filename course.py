from student import Student
from faculty import Faculty

studentList = []
facultyList = []
courseList = []
course_taken_std = []
course_taken_flt = []
numOfStudent = 0
numOfFaculty = 0
numOfCourse = 0

class Course:
    def __init__(self, courseID, courseTitle, credit):
        self.courseID = courseID
        self.courseTitle = courseTitle
        self.credit = credit

    def display_course(self):
        return f"Course ID: {self.courseID}\nCourse: {self.courseTitle}\nCredit Hour: {self.credit}"

    @staticmethod
    def add_student():
        global numOfStudent
        num = int(input("How many students to add? : "))

        for n in range(num):
            name = input("Name of the Student")
            std_id = int(input("Enter his/her ID: "))
            cgpa = float(input("Enter his/her grade"))

            std = Student(std_id, name, cgpa)
            studentList.append(std)
            numOfStudent += 1
            print(f"Student number {n+1} added successfully")

    @staticmethod
    def add_faculty():
        global numOfFaculty
        num = int(input("How many faculties to add? : "))

        for n in range(num):
            name = input("Name of the Faculty")
            flt_id = int(input("Enter his/her ID: "))
            position = input("Enter his/her position")

            flt = Faculty(flt_id, name, position)
            facultyList.append(flt)
            numOfFaculty += 1
            print(f"Faculty number {n + 1} added successfully")

    @staticmethod
    def add_course():
        global numOfCourse
        num = int(input("How many courses to add? : "))

        for n in range(num):
            title = input("Course title: ")
            crs_id = input("Enter course ID: ")
            credit = int(input("Enter credit hour of the course: "))

            crs = Course(crs_id, title, credit)
            courseList.append(crs)
            numOfCourse += 1
            print(f"Course number {n + 1} added successfully")

    @staticmethod
    def del_student(std_del):
        global numOfStudent
        found = False
        for student in studentList:
            if student.student_id == std_del:
                studentList.remove(student)
                numOfStudent -= 1
                print(f"Student: {student.student_name} removed successfully")
                found = True
                break
        if not found:
            print(f"No student found with the id {std_del}")

    @staticmethod
    def del_course(crs_del):
        global numOfCourse
        found = False
        for course in courseList:
            if course.courseID == crs_del:
                courseList.remove(course)
                numOfCourse -= 1
                print(f"Course: {course.courseTitle} removed successfully")
                found = True
                break
        if not found:
            print(f"No course found with the id {crs_del}")


    @staticmethod
    def del_faculty(flt_del):
        global numOfFaculty
        found = False
        for faculty in facultyList:
            if faculty.faculty_id == flt_del:
                facultyList.remove(faculty)
                numOfFaculty -= 1
                print(f"Faculty: {faculty.faculty_name} removed successfully")
                found = True
                break
        if not found:
            print(f"No faculty found with the id {flt_del}")

    @staticmethod
    def upd_student(std_upd):
        found = False
        for student in studentList:
            if student.student_id == std_upd:
                cgpa_upd = float(input("Enter the updated cgpa: "))
                student.student_CGPA = cgpa_upd
                print(f"Student: {student.student_name} information updated successfully")
                found = True
                break
        if not found:
            print(f"No student found with the id {std_upd}")

    @staticmethod
    def upd_course(crs_upd):
        found = False
        for course in courseList:
            if course.courseID == crs_upd:
                credit_upd = int(input("Enter the updated credit hour: "))
                course.credit = credit_upd
                print(f"Course: {course.courseTitle} information updated successfully")
                found = True
                break
        if not found:
            print(f"No course found with the id {crs_upd}")

    @staticmethod
    def upd_faculty(flt_upd):
        found = False
        for faculty in facultyList:
            if faculty.faculty_id == flt_upd:
                position_upd = input("Enter the updated position: ")
                faculty.faculty_position = position_upd
                print(f"Faculty: {faculty.faculty_name} information updated successfully")
                found = True
                break
        if not found:
            print(f"No faculty found with the id {flt_upd}")

    @staticmethod
    def assign_std(std):
        found = False
        num = 1
        for student in studentList:
            if student.student_id == std:
                print("Available Courses: ")
                for course in courseList:
                    print(f"{num}. ", course.display_course())
                    num += 1
                total_courses = int(input("How many courses to take? : "))
                course_taken = []

                for _ in range(total_courses):
                    found_crs = False
                    crs_id = input("Enter the Course ID: ")

                    for course in courseList:
                        if course.courseID == crs_id:
                            if course not in course_taken_std:
                                course_taken.append(course.display_course())
                            else:
                                print(f"{crs_id} is already assigned")
                            found_crs = True
                            break
                    if not found_crs:
                        print(f"No course found with the ID: {crs_id}")

                course_taken_std.append((student.display_student(), course_taken))
                found = True
                break
        if not found:
            print(f"No Student found with the ID: {std}")

    @staticmethod
    def assign_flt(flt):
        found = False
        num = 1
        for faculty in facultyList:
            if faculty.faculty_id == flt:
                print("Available Courses: ")
                for course in courseList:
                    print(f"{num}. ", course.display_course())
                    num += 1
                total_courses = int(input("How many courses to teach? : "))
                course_taken = []

                for _ in range(total_courses):
                    found_crs = False
                    crs_id = input("Enter the Course ID: ")

                    for course in courseList:
                        if course.courseID == crs_id:
                            if course not in course_taken:
                                course_taken.append(course.display_course())
                            else:
                                print(f"{crs_id} is already assigned")
                            found_crs = True
                            break
                    if not found_crs:
                        print(f"No course found with the ID: {crs_id}")

                course_taken_flt.append((faculty.display_faculty(), course_taken))
                found = True
                break
        if not found:
            print(f"No Student found with the ID: {flt}")

    @staticmethod
    def std_crs():
        if not course_taken_std:
            print("No courses assigned to student(s) yet")
        else:
            for std_info, crs in course_taken_std:
                print("\nStudent Info:")
                print(std_info)
                print("Assigned Course:")
                for course in crs:
                    print(f"- {course}")

    @staticmethod
    def flt_crs():
        if not course_taken_flt:
            print("No courses assigned to faculty(s) yet")
        else:
            for flt_info, crs in course_taken_flt:
                print("\nFaculty Info:")
                print(flt_info)
                print("Assigned Course:")
                for course in crs:
                    print(f"- {course}")
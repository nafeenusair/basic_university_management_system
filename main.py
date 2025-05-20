from University.course import studentList, facultyList
from course import Course, courseList

def main():
    while True:
        print("___X University___")
        print("a. Add")
        print("b. Delete")
        print("c. Update")
        print("d. Assign course(s) to student")
        print("e. Assign course(s) to faculty")
        print("f. Print")
        print("g. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case 'a':
                print("a. Add a Student")
                print("b. Add a Course")
                print("c. Add a Faculty")
                choice_add = input("Enter your choice: ")

                match choice_add:
                    case 'a':
                        Course.add_student()
                    case 'b':
                        Course.add_course()
                    case 'c':
                        Course.add_faculty()
                    case _:
                        print("Invalid Input! Try Again")
            case 'b':
                print("a. Delete a Student")
                print("b. Delete a Course")
                print("c. Delete a Faculty")
                choice_del = input("Enter your choice: ")

                match choice_del:
                    case 'a':
                        std_del = int(input("Enter the ID of the student to remove: "))
                        Course.del_student(std_del)
                    case 'b':
                        crs_del = input("Enter the course ID to remove: ")
                        Course.del_course(crs_del)
                    case 'c':
                        flt_del = int(input("Enter the ID of the faculty to remove: "))
                        Course.del_faculty(flt_del)
                    case _:
                        print("Invalid Input! Try Again")
            case 'c':
                print("a. Update a Student")
                print("b. Update a Course")
                print("c. Update a Faculty")
                choice_update = input("Enter your choice: ")

                match choice_update:
                    case 'a':
                        std_upd = int(input("Enter the ID of the student to update: "))
                        Course.upd_student(std_upd)
                    case 'b':
                        crs_upd = input("Enter the course ID to update: ")
                        Course.upd_course(crs_upd)
                    case 'c':
                        flt_upd = int(input("Enter the ID of the faculty to update: "))
                        Course.upd_faculty(flt_upd)
                    case _:
                        print("Invalid Input! Try Again")
            case 'd':
                std = int(input("Enter the ID of the student to assign course: "))
                Course.assign_std(std)
            case 'e':
                flt = int(input("Enter the ID of the faculty to assign course: "))
                Course.assign_flt(flt)
            case 'f':
                print("a. Print all students")
                print("b. Print all courses")
                print("c. Print all faculties")
                print("d. Print information of a student")
                print("e. Print information of a course")
                print("f. Print information of a faculty")
                print("g. Print students full information")
                print("h. Print faculties full information")
                choice_print = input("Enter your choice: ")

                match choice_print:
                    case 'a':
                        if not studentList:
                            print("No Student to display")
                        else:
                            for student in studentList:
                                print(student.display_student())
                    case 'b':
                        if not courseList:
                            print("No Course to display")
                        else:
                            for course in courseList:
                                print(course.display_course())
                    case 'c':
                        if not facultyList:
                            print("No Faculty to display")
                        else:
                            for faculty in facultyList:
                                print(faculty.display_faculty())
                    case 'd':
                        std_info = int(input("Enter the ID of the student: "))
                        found = False
                        for student in studentList:
                            if student.student_id == std_info:
                                print(student.display_student())
                                found = True
                                break
                        if not found:
                            print(f"Student with ID {std_info} not found")
                    case 'e':
                        crs_info = input("Enter the course ID: ")
                        found = False
                        for course in courseList:
                            if course.courseID == crs_info:
                                print(course.display_course())
                                found = True
                                break
                        if not found:
                            print(f"Course with ID '{crs_info}' not found")
                    case 'f':
                        flt_info = int(input("Enter the ID of the faculty: "))
                        found = False
                        for faculty in facultyList:
                            if faculty.faculty_id == flt_info:
                                print(faculty.display_faculty())
                                found = True
                                break
                        if not found:
                            print(f"Faculty with ID {flt_info} not found")
                    case 'g':
                        Course.std_crs()
                    case 'h':
                        Course.flt_crs()
            case 'g':
                print("Exiting!")
                break
            case _:
                print("Invalid Input! Please Try Again....")

if __name__ == "__main__":
    main()

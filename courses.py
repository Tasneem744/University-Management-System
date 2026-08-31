class Department:

    def __init__(self, department_id: int, name: str):

        self.department_id = department_id
        self.name = name
        self.courses = []
        self.instructors = []


    def add_course(self, course):

        if course is None:
            print("Error: Cannot add an empty course")
            return False

        if course in self.courses:
            print("Course already exists in this department")
            return False

        self.courses.append(course)
        return True


    def add_instructor(self, instructor):

        if instructor is None:
            print("Error: Cannot add an empty instructor")
            return False

        if instructor in self.instructors:
            print("Instructor already exists in this department")
            return False

        self.instructors.append(instructor)
        return True


    def display_info(self):

        return f"""
            Department ID: {self.department_id}
            Name: {self.name}
            Courses Count: {len(self.courses)}
            Instructors Count: {len(self.instructors)}
        """


class Course:

    def __init__(
        self,
        course_code: str,
        title: str,
        credit_hours: int,
        department=None
    ):

        self.course_code = course_code
        self.title = title
        self.credit_hours = credit_hours
        self.department = department
        self.instructor = None
        self.students = []

        if department is not None:
            department.add_course(self)


    def assign_instructor(self, instructor):

        if instructor is None:
            print("Error: Instructor cannot be empty.")
            return False

        if self.instructor is not None:
            print("This course already has an instructor.")
            return False

        self.instructor = instructor

        if self not in instructor.assigned_courses:
            instructor.assigned_courses.append(self)

        if self.department is not None:
            self.department.add_instructor(instructor)

        print(
            f"{instructor.get_name()} assigned to {self.title} successfully."
        )

        return True


    def add_student(self, student):

        if student is None:
            print("Error: Student cannot be empty")
            return False

        if student in self.students:
            print("Student is already enrolled in this course")
            return False

        self.students.append(student)

        return True


    def remove_student(self, student_id):

        if not self.students:
            print("No students are enrolled in this course")
            return False

        for student in self.students:

            if student.get_id() == student_id:

                self.students.remove(student)

                print("Student removed successfully")

                return True

        print("Student not found in this course")

        return False


    def display_info(self):

        if self.instructor is not None:
            instructor_name = self.instructor.get_name()
        else:
            instructor_name = "Not Assigned"

        if self.department is not None:
            department_name = self.department.name
        else:
            department_name = "General"

        return f"""
            Course: {self.course_code} - {self.title}
            Credits: {self.credit_hours}
            Department: {department_name}
            Instructor: {instructor_name}
            Students Count: {len(self.students)}
        """

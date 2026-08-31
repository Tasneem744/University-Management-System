class Department:

    def __init__(self, department_id: int, name: str):
        self.department_id = department_id
        self.name = name
        self.courses = []
        self.instructors = []

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def add_instructor(self, instructor):
        if instructor not in self.instructors:
            self.instructors.append(instructor)

    def display_info(self):
        return (
            f"Department ID: {self.department_id}\n"
            f"Name: {self.name}\n"
            f"Courses Count: {len(self.courses)}\n"
            f"Instructors Count: {len(self.instructors)}"
        )


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

        
        if department:
            department.add_course(self)


    def assign_instructor(self, instructor):

        self.instructor = instructor

        
        if self not in instructor.assigned_courses:
            instructor.assigned_courses.append(self)

        if self.department:
            self.department.add_instructor(instructor)


    def add_student(self, student):

        if student not in self.students:
            self.students.append(student)


    def remove_student(self, student_id):

     for student in self.students:

        if student.person_id == student_id:
            self.students.remove(student)
            break


    def display_info(self):

     if self.instructor:
        instructor_name = self.instructor.name
     else:
        instructor_name = "Not Assigned"

     if self.department:
        department_name = self.department.name
     else:
        department_name = "General"

     return (
        f"Course: {self.course_code} - {self.title}\n"
        f"Credits: {self.credit_hours}\n"
        f"Department: {department_name}\n"
        f"Instructor: {instructor_name}"
     )
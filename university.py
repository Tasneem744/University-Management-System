from enrollment import Enrollment, Grade


class UniversitySystem:
    def __init__(self, name="DEPI University System"):
        self.name = name
        self.students = []
        self.instructors = []
        self.courses = []
        self.departments = []
        self.enrollments = []

    def add_student(self, student):
        if student is None:
            return False

        existing_student = self.search_student(student.get_id())
        if existing_student is not None:
            return False

        self.students.append(student)
        return True

    def add_instructor(self, instructor):
        if instructor is None:
            return False

        existing_instructor = self.search_instructor(instructor.get_id())
        if existing_instructor is not None:
            return False

        self.instructors.append(instructor)
        return True

    def add_course(self, course):
        if course is None:
            return False

        existing_course = self.search_course(course.course_code)
        if existing_course is not None:
            return False

        self.courses.append(course)
        return True

    def add_department(self, department):
        if department is None:
            return False

        for dept in self.departments:
            if dept.department_id == department.department_id or dept.name == department.name:
                return False

        self.departments.append(department)
        return True

    def search_student(self, identifier):
        for student in self.students:
            if student.get_id() == identifier or student.get_name() == identifier:
                return student
        return None

    def search_instructor(self, identifier):
        for instructor in self.instructors:
            if instructor.get_id() == identifier or instructor.get_name() == identifier:
                return instructor
        return None

    def search_person(self, identifier):
        """Generic search using Inheritance (Person polymorphic lookup)"""
        student = self.search_student(identifier)
        if student:
            return student
        return self.search_instructor(identifier)

    def update_student(self, student_id, new_name=None):
        """Required Update Operation (Section 7.D)"""
        student = self.search_student(student_id)
        if student is None:
            return False

        if new_name:
            student.set_name(new_name)
        return True

    def search_course(self, identifier):
        for course in self.courses:
            if course.course_code == identifier or course.title == identifier:
                return course
        return None

    def enroll_student_in_course(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)

        if student is None or course is None:
            return False

        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id() and enrollment.course.course_code == course.course_code:
                return False

        new_enrollment = Enrollment(student, course)
        self.enrollments.append(new_enrollment)
        return True

    def remove_student_from_course(self, student_id, course_code):
        student = self.search_student(student_id)
        course = self.search_course(course_code)

        if student is None or course is None:
            return False

        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id() and enrollment.course.course_code == course.course_code:
                self.enrollments.remove(enrollment)
                course.remove_student(student.get_id())
                return True

        return False

    def assign_instructor_to_course(self, instructor_id, course_code):
        instructor = self.search_instructor(instructor_id)
        course = self.search_course(course_code)

        if instructor is None or course is None:
            return False

        return course.assign_instructor(instructor)

    def record_grade(self, student_id, course_code, midterm, final, assignments):
        student = self.search_student(student_id)
        course = self.search_course(course_code)

        if student is None or course is None:
            return False

        target_enrollment = None
        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id() and enrollment.course.course_code == course.course_code:
                target_enrollment = enrollment
                break

        if target_enrollment is None:
            return False

        grade_obj = Grade(midterm=midterm, final=final, assignments=assignments)
        target_enrollment.assign_grade(grade_obj)
        return True

    def calculate_student_average(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            return 0.0

        total_points = 0.0
        total_hours = 0

        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id() and enrollment.has_grade():
                grade_total = enrollment.get_grade().get_total_grade()
                credit_hours = enrollment.course.credit_hours

                total_points += (grade_total * credit_hours)
                total_hours += credit_hours

        if total_hours == 0:
            return 0.0

        percentage_avg = total_points / total_hours
        gpa_4_scale = (percentage_avg / 100.0) * 4.0
        student.set_gpa(gpa_4_scale)

        return percentage_avg

    def display_student_courses(self, student_id):
        student = self.search_student(student_id)
        if student is None:
            print("Student not found.")
            return

        print(f"Courses for student {student.get_name()}:")
        for enrollment in self.enrollments:
            if enrollment.student.get_id() == student.get_id():
                if enrollment.has_grade():
                    print(f"- {enrollment.course.title}: {enrollment.get_grade().get_total_grade()} ({enrollment.get_grade().get_letter_grade()})")
                else:
                    print(f"- {enrollment.course.title}: No grade yet")

    def display_course_students(self, course_code):
        course = self.search_course(course_code)
        if course is None:
            print("Course not found.")
            return

        print(f"Students enrolled in {course.title}:")
        for student in course.students:
            print(f"- {student.get_name()} (ID: {student.get_id()})")

    def display_department_info(self, department_name):
        dept = None
        for d in self.departments:
            if d.name == department_name:
                dept = d
                break

        if dept is None:
            print("Department not found.")
            return

        print(dept.display_info())
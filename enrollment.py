from datetime import date


class Grade:
    def __init__(self, midterm=0.0, final=0.0, assignments=0.0):
        self.set_midterm(midterm)
        self.set_final(final)
        self.set_assignments(assignments)

    def _validate_score(self, score, label):
        if not 0 <= score <= 100:
            raise ValueError(
                f"Invalid {label} score: '{score}'. Must be between 0 and 100."
            )

    def set_midterm(self, midterm):
        self._validate_score(midterm, "Midterm")
        self.__midterm = midterm

    def set_final(self, final):
        self._validate_score(final, "Final")
        self.__final = final

    def set_assignments(self, assignments):
        self._validate_score(assignments, "Assignments")
        self.__assignments = assignments

    def get_midterm(self):
        return self.__midterm

    def get_final(self):
        return self.__final

    def get_assignments(self):
        return self.__assignments

    def get_total_grade(self):
        total = (
            (self.__midterm * 0.30)
            + (self.__final * 0.50)
            + (self.__assignments * 0.20)
        )
        return round(total, 2)

    def get_letter_grade(self):
        total = self.get_total_grade()
        if total >= 90:
            return "A"
        elif total >= 80:
            return "B"
        elif total >= 70:
            return "C"
        elif total >= 60:
            return "D"
        else:
            return "F"

    def display_grade(self):
        return (
            f"Midterm: {self.__midterm}/100 | "
            f"Final: {self.__final}/100 | "
            f"Assignments: {self.__assignments}/100 | "
            f"Total: {self.get_total_grade()} | "
            f"Letter: {self.get_letter_grade()}"
        )


class Enrollment:
    _id_counter = 1

    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = date.today()
        self.__grade = None

        self._enrollment_id = f"E-{Enrollment._id_counter:03d}"
        Enrollment._id_counter += 1

        course.add_student(student)

    def get_id(self):
        return self._enrollment_id

    def assign_grade(self, grade: Grade):
        if not isinstance(grade, Grade):
            raise ValueError("assign_grade() expects a Grade object.")
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def has_grade(self):
        return self.__grade is not None

    def display_enrollment_details(self):
        print("\n" + "-" * 50)
        print(f"Enrollment ID: {self._enrollment_id}")
        print(f"Student: {self.student.get_name()} ({self.student.get_id()})")
        print(f"Course: {self.course.course_code} - {self.course.title}")
        print(f"Enrollment Date: {self.enrollment_date}")
        if self.has_grade():
            print(f"Grade -> {self.__grade.display_grade()}")
        else:
            print("Grade: Not graded yet")
        print("-" * 50)

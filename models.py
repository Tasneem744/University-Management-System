from abc import ABC, abstractmethod
import re


class Person(ABC):
    _id_counter = 1

    def __init__(self, name, age, email):
        self.set_name(name)
        self.set_age(age)
        self.set_email(email)

        self._id = f"P-{Person._id_counter:03d}"
        Person._id_counter += 1

    def display_info(self):
        print("\n" + "=" * 50)
        print(f"{self.__class__.__name__} Information")
        print("=" * 50)
        print(
            f"ID: {self._id}\n"
            f"Name: {self.get_name()}\n"
            f"Age: {self.get_age()}\n"
            f"Email: {self.get_email()}"
        )

    def get_id(self):
        return self._id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if not new_name.strip() or not all(
            char.isalpha() or char.isspace()
            for char in new_name
        ):
            raise ValueError(f"Invalid Name: '{new_name}'")

        self.__name = new_name.strip()

    def get_age(self):
        return self.__age

    @abstractmethod
    def set_age(self, new_age):
        pass

    def _assign_age(self, age):
        self.__age = age

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

        if not re.match(pattern, new_email):
            raise ValueError(
                f"Invalid Email: '{new_email}'"
            )

        self.__email = new_email


class Student(Person):

    def __init__(self, name, age, email, level, gpa=0.0):
        super().__init__(name, age, email)

        self._level = level
        self.__gpa = 0.0
        self.set_gpa(gpa)

    def set_age(self, new_age):
        if not 16 <= new_age <= 30:
            raise ValueError(
                f"Invalid Student Age: '{new_age}'. "
                "Age must be between 16 and 30."
            )

        self._assign_age(new_age)

    def display_info(self):
        super().display_info()

        print(f"Level: {self._level}")
        print(f"GPA: {self.__gpa:.2f}")
        print("=" * 50)

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if not 0.0 <= gpa <= 4.0:
            raise ValueError(
                f"Invalid GPA: '{gpa}'. "
                "GPA must be between 0.0 and 4.0."
            )

        self.__gpa = gpa


class Instructor(Person):

    def __init__(
        self,
        name,
        age,
        email,
        specialization,
        salary
    ):
        super().__init__(name, age, email)

        if salary < 0:
            raise ValueError(
                f"Invalid Salary: '{salary}'. "
                "Salary cannot be negative."
            )

        self._specialization = specialization
        self.__salary = salary
        self.assigned_courses = []    
    def set_age(self, new_age):
        if not 22 <= new_age <= 80:
            raise ValueError(
                f"Invalid Instructor Age: '{new_age}'. "
                "Age must be between 22 and 80."
            )

        self._assign_age(new_age)

    def display_info(self):
        super().display_info()

        print(f"Specialization: {self._specialization}")
        print(f"Salary: ${self.__salary}")
        print(f"Assigned Courses: {len(self.assigned_courses)}")
        print("=" * 50)

    def increase_salary(self, amount):
        if amount <= 0:
            raise ValueError(
                "Salary increase amount must be positive."
            )

        self.__salary += amount

    def get_salary(self):
        return self.__salary   
    
    def remove_course(self, course):

        if course not in self.assigned_courses:
            print("Course is not assigned to this instructor")
            return False

        self.assigned_courses.remove(course)

        
        if course.instructor == self:
            course.instructor = None

        print("Course removed successfully")

        return True



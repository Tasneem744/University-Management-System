from models import Student, Instructor
from courses import Department, Course
from enrollment import Enrollment
from university import UniversitySystem
# 1) Create the central system
system = UniversitySystem()
# 2) Create a department and register it
cs_department = Department(1, "Computer Science")
system.add_department(cs_department)
# 3) Create courses under the department (auto-registers with department)
course1 = Course("CS101", "Intro to Python OOP", 3, department=cs_department)
course2 = Course("CS102", "Data Structures", 4, department=cs_department)
system.add_course(course1)
system.add_course(course2)
# 4) Create instructors and register them
instructor1 = Instructor("Ahmed Hassan", 40, "ahmed.hassan@uni.edu", "Software Engineering", 15000)
instructor2 = Instructor("Sara Adel", 38, "sara.adel@uni.edu", "Algorithms", 14000)
system.add_instructor(instructor1)
system.add_instructor(instructor2)
# 5) Assign instructors to courses (relationship operation)
system.assign_instructor_to_course(instructor1.get_id(), "CS101")
system.assign_instructor_to_course(instructor2.get_id(), "CS102")
# 6) Create students and register them
student1 = Student("Mona Khaled", 20, "mona.khaled@uni.edu", "Junior")
student2 = Student("Omar Tarek", 21, "omar.tarek@uni.edu", "Senior")
student3 = Student("Laila Fathy", 19, "laila.fathy@uni.edu", "Freshman")
system.add_student(student1)
system.add_student(student2)
system.add_student(student3)
# 7) Enroll students in courses (relationship operation)
system.enroll_student_in_course(student1.get_id(), "CS101")
system.enroll_student_in_course(student1.get_id(), "CS102")
system.enroll_student_in_course(student2.get_id(), "CS101")
system.enroll_student_in_course(student3.get_id(), "CS102")
# 8) Record grades (midterm, final, assignments out of 100 each)
system.record_grade(student1.get_id(), "CS101", midterm=90, final=95, assignments=100)
system.record_grade(student1.get_id(), "CS102", midterm=80, final=85, assignments=90)
system.record_grade(student2.get_id(), "CS101", midterm=70, final=75, assignments=80)
system.record_grade(student3.get_id(), "CS102", midterm=85, final=88, assignments=92)
# 9) Calculate and display each student's average
print("\n--- Student Averages ---")
for student in (student1, student2, student3):
    avg = system.calculate_student_average(student.get_id())
    print(f"{student.get_name()}'s average: {avg:.2f}% | GPA (4.0 scale): {student.get_gpa():.2f}")

# 10) Display full info for a student and an instructor
print("\n--- Full Person Info ---")
student1.display_info()
instructor1.display_info()
# 11) Display student courses / course students / department info
print("\n--- Student Courses ---")
system.display_student_courses(student1.get_id())

print("\n--- Course Students ---")
system.display_course_students("CS101")

print("\n--- Department Info ---")
system.display_department_info("Computer Science")
# 12) Search demonstration
print("\n--- Search Demonstration ---")
found_student = system.search_student(student2.get_id())
if found_student:
    print(f"Found student: {found_student.get_name()}")

found_course = system.search_course("CS999")  # non-existing course
if found_course is None:
    print("Course CS999 not found (as expected)")

# 13) Update demonstration
print("\n--- Update Demonstration ---")
system.update_student(student2.get_id(), new_name="Omar Tarek Ali")
print(f"Updated name: {system.search_student(student2.get_id()).get_name()}")

# 14)  display course's students 
print("\n--- Course Students ---")
system.display_course_students("CS102")
# 15) Remove demonstration (remove a student from a course, not from the system)
print("\n--- Remove Demonstration ---")
system.remove_student_from_course(student3.get_id(), "CS102")
# 16)  display course's students 
print("\n--- Course Students ---")
system.display_course_students("CS102")
# 17) Validation case: enroll a student in a non-existing course
print("\n--- Validation Case ---")
result = system.enroll_student_in_course(student1.get_id(), "CS999")
if not result:
    print("Enrollment failed: Course CS999 does not exist (handled gracefully)")
# Base class representing a person (Student or Teacher)
class Person:
    def __init__(self, name, age, person_id):
        self.name = name
        self.age = age
        self.person_id = person_id


# Class representing a student
class Student(Person):
    def __init__(self, name, age, student_id, grade):
        super().__init__(name, age, student_id)
        self.grade = grade
        self.enrolled_courses = []  # List to store courses the student is enrolled in

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        course.enroll_student(self)  # Enroll in the course as well


# Class representing a teacher
class Teacher(Person):
    def __init__(self, name, age, teacher_id, subject):
        super().__init__(name, age, teacher_id)
        self.subject = subject
        self.assigned_courses = []  # List to store courses the teacher is assigned to

    def assign_course(self, course):
        self.assigned_courses.append(course)
        course.assign_teacher(self)  # Assign the teacher to the course


# Class representing a course
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []  # List to store students enrolled in the course
        self.teacher = None  # To store the assigned teacher

    def enroll_student(self, student):
        self.enrolled_students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def average_grade(self):
        if not self.enrolled_students:
            return 0
        total_grade = sum(student.grade for student in self.enrolled_students)
        return total_grade / len(self.enrolled_students)


# Class representing the school
class School:
    def __init__(self):
        self.students = []  # List to store all students
        self.teachers = []  # List to store all teachers
        self.courses = []   # List to store all courses

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def enroll_student_in_course(self, student_id, course_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            student.enroll_in_course(course)
            print(f"{student.name} has been enrolled in {course.course_name}.")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = next((t for t in self.teachers if t.person_id == teacher_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if teacher and course:
            teacher.assign_course(course)
            print(f"{teacher.name} has been assigned to teach {course.course_name}.")

    def view_students_in_course(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            print(f"Students enrolled in {course.course_name}:")
            for student in course.enrolled_students:
                print(f"- {student.name} (Grade: {student.grade})")

    def view_courses_of_student(self, student_id):
        student = next((s for s in self.students if s.person_id == student_id), None)
        if student:
            print(f"{student.name} is enrolled in the following courses:")
            for course in student.enrolled_courses:
                print(f"- {course.course_name}")

    def calculate_average_grade(self, course_id):
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if course:
            average = course.average_grade()
            print(f"The average grade in {course.course_name} is {average:.2f}.")


# Example usage of the system
school = School()

# Creating students
student1 = Student("Aditya", 19, "S001", 94)
student2 = Student("Student2", 21, "S002", 79)
student2 = Student("Student3", 20, "S003", 85)
student2 = Student("Student4", 20, "S004", 90)
student2 = Student("Student5", 19, "S005", 81)

# Creating teachers
teacher1 = Teacher("Mr. Dubey", 40, "T001", "Math")
teacher2 = Teacher("Ms. Kulkarni", 35, "T002", "Science")

# Creating courses
course1 = Course("Math 101", "C001")
course2 = Course("Science 101", "C002")

# Adding students, teachers, and courses to the school
school.add_student(student1)
school.add_student(student2)
school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_course(course1)
school.add_course(course2)

# Enroll students in courses
school.enroll_student_in_course("S001", "C001")
school.enroll_student_in_course("S002", "C001")
school.enroll_student_in_course("S002", "C002")

# Assign teachers to courses
school.assign_teacher_to_course("T001", "C001")
school.assign_teacher_to_course("T002", "C002")

# View students in a course
school.view_students_in_course("C001")

# View courses of a student
school.view_courses_of_student("S002")

# Calculate the average grade in a course
school.calculate_average_grade("C001")

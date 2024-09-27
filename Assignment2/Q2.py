# Sample student data
students_data = [
    {"student_name": "Aditya", "grades": {"Math": 95, "Science": 89, "English": 91}},
    {"student_name": "Kartik", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Shyam", "grades": {"Math": 88, "Science": 76, "English": 94}},
]

# 1. Calculate average grade for each student
def calculate_average(grades):
    total = sum(grades.values())
    return total / len(grades)

# 2. Determine the top-performing student
top_student = None
top_average = 0

for student in students_data:
    average_grade = calculate_average(student["grades"])
    if average_grade > top_average:
        top_average = average_grade
        top_student = student

# 3. Find the highest and lowest grades across all students
highest_grade = None
lowest_grade = None

for student in students_data:
    for subject, grade in student["grades"].items():
        if highest_grade is None or grade > highest_grade:
            highest_grade = grade
        if lowest_grade is None or grade < lowest_grade:
            lowest_grade = grade

# 4. Categorize students based on performance (A: 90+, B: 80-89, C: 70-79, etc.)
grade_distribution = {"A": [], "B": [], "C": [], "D": [], "F": []}

for student in students_data:
    average_grade = calculate_average(student["grades"])
    
    if average_grade >= 90:
        grade_distribution["A"].append(student["student_name"])
    elif average_grade >= 80:
        grade_distribution["B"].append(student["student_name"])
    elif average_grade >= 70:
        grade_distribution["C"].append(student["student_name"])
    elif average_grade >= 60:
        grade_distribution["D"].append(student["student_name"])
    else:
        grade_distribution["F"].append(student["student_name"])

# Output results
print("Average Grades per Student:")
for student in students_data:
    print(f"{student['student_name']}: {calculate_average(student['grades']):.2f}")

print(f"\nTop-performing student: {top_student['student_name']} with an average grade of {top_average:.2f}")

print(f"\nHighest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")

print("\nGrade Distribution:")
for grade, students in grade_distribution.items():
    print(f"{grade}: {', '.join(students) if students else 'None'}")

# Sample student data
students_data = [
    {"student_name": "Aditya", "grades": {"Math": 95, "Science": 89, "English": 91}},
    {"student_name": "Kartik", "grades": {"Math": 85, "Science": 92, "English": 78}},
    {"student_name": "Shyam", "grades": {"Math": 88, "Science": 76, "English": 94}},
]

# Calculate average grade for a student
def calculate_average(grades):
    return sum(grades.values()) / len(grades)

# Initialize variables
top_student, top_average = None, 0
highest_grade, lowest_grade = None, None
grade_distribution = {"A": [], "B": [], "C": [], "D": [], "F": []}

# Process student data
for student in students_data:
    avg = calculate_average(student["grades"])
    if avg > top_average:  # Track top-performing student
        top_average, top_student = avg, student["student_name"]

    for grade in student["grades"].values():  # Find highest and lowest grades
        highest_grade = grade if highest_grade is None or grade > highest_grade else highest_grade
        lowest_grade = grade if lowest_grade is None or grade < lowest_grade else lowest_grade

    # Categorize student into grade distribution
    if avg >= 90: grade_distribution["A"].append(student["student_name"])
    elif avg >= 80: grade_distribution["B"].append(student["student_name"])
    elif avg >= 70: grade_distribution["C"].append(student["student_name"])
    elif avg >= 60: grade_distribution["D"].append(student["student_name"])
    else: grade_distribution["F"].append(student["student_name"])

# Output results
print(f"Top student: {top_student} with average {top_average:.2f}")
print(f"Highest grade: {highest_grade}, Lowest grade: {lowest_grade}")
print("Grade Distribution:", grade_distribution)

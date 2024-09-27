from datetime import datetime

# Sample attendance data
attendance_data = [
    {
        "employee_name": "Raju",
        "attendance": {
            "2024-08-15": ("09:00", "17:00"),
            "2024-08-16": ("09:15", "17:10"),
        },
    },
    {
        "employee_name": "Shyam",
        "attendance": {
            "2024-08-15": ("09:30", "16:30"),
            "2024-08-16": ("09:00", "17:00"),
        },
    },
    {
        "employee_name": "Baburao",
        "attendance": {
            "2024-08-15": ("09:10", "16:50"),
        },
    },
]

# Function to calculate hours worked
def calculate_hours(clock_in, clock_out):
    in_time = datetime.strptime(clock_in, "%H:%M")
    out_time = datetime.strptime(clock_out, "%H:%M")
    return (out_time - in_time).seconds / 3600  # Convert seconds to hours

# Initialize tracking variables
total_hours_worked = {}
absences = {}
perfect_attendance = []

# Process attendance data
for employee in attendance_data:
    name = employee["employee_name"]
    attendance = employee["attendance"]
    
    # Calculate total hours worked
    total_hours = sum(calculate_hours(times[0], times[1]) for times in attendance.values())
    total_hours_worked[name] = total_hours
    
    # Track absences and perfect attendance
    absences[name] = 2 - len(attendance)  # Assuming 2 workdays for simplicity
    if absences[name] == 0:
        perfect_attendance.append(name)

# Find employee with most absences
most_absences = max(absences, key=absences.get)

# Output results
print("Total hours worked per employee:")
for name, hours in total_hours_worked.items():
    print(f"{name}: {hours:.2f} hours")

print(f"\nEmployees with perfect attendance: {perfect_attendance}")
print(f"Employee with most absences: {most_absences}")

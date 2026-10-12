import json
from datetime import datetime


JSON_FILE = "attendance.json"

START_DATE = "2026-10-08"
END_DATE = "2026-10-14"


def load_data():
    """Load attendance data from JSON file."""

    with open(JSON_FILE, "r") as file:
        return json.load(file)


def save_data(data):
    """Save updated attendance data to JSON file."""

    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=2)


def validate_date(date):
    """Check whether the date is within the allowed attendance period."""

    try:
        requested_date = datetime.strptime(date, "%Y-%m-%d")
        start = datetime.strptime(START_DATE, "%Y-%m-%d")
        end = datetime.strptime(END_DATE, "%Y-%m-%d")

        return start <= requested_date <= end

    except ValueError:
        return False


def find_student(data, roll_no):
    """Find a student using roll number."""

    for student in data["students"]:
        if student["roll_no"] == str(roll_no):
            return student

    return None


def calculate_percentage(student):
    """Calculate attendance percentage."""

    attendance = student["attendance"]

    total_days = len(attendance)
    present_days = sum(
        1 for status in attendance.values()
        if status is True
    )

    if total_days == 0:
        percentage = 0
    else:
        percentage = (present_days / total_days) * 100

    return {
        "present_days": present_days,
        "total_days": total_days,
        "attendance_percentage": round(percentage, 2)
    }


def check_attendance(roll_no, date):
    """Check whether a student was present on a particular date."""

    data = load_data()

    student = find_student(data, roll_no)

    if student is None:
        return {
            "success": False,
            "error": "Student not found"
        }

    if not validate_date(date):
        return {
            "success": False,
            "error": "Date must be between 2026-10-08 and 2026-10-14"
        }

    if date not in student["attendance"]:
        return {
            "success": False,
            "error": "Attendance record not found for this date"
        }

    return {
        "success": True,
        "action": "check_attendance",
        "name": student["name"],
        "roll_no": student["roll_no"],
        "date": date,
        "present": student["attendance"][date]
    }


def mark_attendance(roll_no, date):
    """Mark a student present."""

    data = load_data()

    student = find_student(data, roll_no)

    if student is None:
        return {
            "success": False,
            "error": "Student not found"
        }

    if not validate_date(date):
        return {
            "success": False,
            "error": "Date must be between 2026-10-08 and 2026-10-14"
        }

    student["attendance"][date] = True

    save_data(data)

    percentage = calculate_percentage(student)

    return {
        "success": True,
        "action": "mark_attendance",
        "name": student["name"],
        "roll_no": student["roll_no"],
        "date": date,
        "present": True,
        "attendance_percentage": percentage["attendance_percentage"]
    }


def remove_attendance(roll_no, date):
    """Remove attendance by marking the student absent."""

    data = load_data()

    student = find_student(data, roll_no)

    if student is None:
        return {
            "success": False,
            "error": "Student not found"
        }

    if not validate_date(date):
        return {
            "success": False,
            "error": "Date must be between 2026-10-08 and 2026-10-14"
        }

    student["attendance"][date] = False

    save_data(data)

    percentage = calculate_percentage(student)

    return {
        "success": True,
        "action": "remove_attendance",
        "name": student["name"],
        "roll_no": student["roll_no"],
        "date": date,
        "present": False,
        "attendance_percentage": percentage["attendance_percentage"]
    }


def get_student_percentage(roll_no):
    """Get attendance percentage of one student."""

    data = load_data()

    student = find_student(data, roll_no)

    if student is None:
        return {
            "success": False,
            "error": "Student not found"
        }

    result = calculate_percentage(student)

    return {
        "success": True,
        "action": "calculate_percentage",
        "name": student["name"],
        "roll_no": student["roll_no"],
        **result
    }


def get_class_average():
    """Calculate average attendance percentage of all students."""

    data = load_data()

    percentages = []

    for student in data["students"]:
        result = calculate_percentage(student)
        percentages.append(result["attendance_percentage"])

    if not percentages:
        average = 0
    else:
        average = sum(percentages) / len(percentages)

    return {
        "success": True,
        "action": "class_average",
        "number_of_students": len(percentages),
        "student_percentages": percentages,
        "class_attendance_average": round(average, 2)
    }

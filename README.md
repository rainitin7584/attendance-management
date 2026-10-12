# AI-Based Attendance Management System
# AI Attendance Management System

## 1. Project Overview

The **AI Attendance Management System** is a terminal-based Python application that uses an AI model to understand natural-language attendance requests and perform attendance operations on student data stored in a JSON file.

The system allows users to check attendance percentages, verify whether a student was present on a particular date, mark attendance as present or absent, and calculate the class attendance average.

The project combines Artificial Intelligence with Python programming, JSON file handling, and mathematical calculations. It does not require a frontend or a database.

## 2. Objectives

- Manage student attendance through terminal commands.
- Use an AI model to understand natural-language requests.
- Store student records in a JSON file.
- Calculate individual attendance percentages using Python.
- Calculate the average attendance percentage of the class.
- Update and save attendance changes automatically.
- Validate student details, dates, and attendance operations.

## 3. Features

- **Natural-Language Input:** Enter attendance requests in simple English.
- **Attendance Percentage:** Calculate the attendance percentage of individual students.
- **Daily Attendance Check:** Check whether a student was present on a particular date.
- **Mark Attendance:** Mark a student as present or absent.
- **JSON File Updates:** Save changes directly to `attendance.json`.
- **Class Average:** Calculate the average of all students' attendance percentages.
- **Data Validation:** Check student roll numbers, dates, and valid operations.
- **Terminal Interface:** Interact with the system without a graphical user interface.
- **Persistent Storage:** Retain changes between program runs.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main application logic |
| JSON | Store student attendance records |
| AI Model API | Understand natural-language requests |
| OpenAI Python SDK | Connect to an OpenAI-compatible API |
| python-dotenv | Load API credentials from environment variables |
| Terminal | Accept commands and display results |

## 5. Project Structure

```text
attendance-management/
│
├── main.py
├── attendance.json
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

**File descriptions:**

- `main.py` — Main Python program containing AI integration, attendance operations, calculations, validation, and terminal interaction.
- `attendance.json` — Stores student information and daily attendance records.
- `.env` — Stores the API key securely.
- `.gitignore` — Prevents sensitive files from being uploaded to GitHub.
- `requirements.txt` — Lists the Python dependencies.
- `README.md` — Provides project documentation and setup instructions.

## 6. Attendance Period

The project is designed to manage attendance for five days, from **8 October 2026 to 12 October 2026**, inclusive.

Each student record contains:

- Student name
- Roll number
- Daily attendance status
- Total number of attendance days
- Number of days present
- Attendance percentage

The date range can be modified according to project requirements.

## 7. Sample JSON Data

The following example shows the structure of a student record in `attendance.json`.

```json
{
  "name": "Rahul Sharma",
  "roll_no": "101",
  "attendance": {
    "2026-10-08": true,
    "2026-10-09": true,
    "2026-10-10": false,
    "2026-10-11": true,
    "2026-10-12": true
  },
  "total_days": 5,
  "days_present": 4,
  "attendance_percentage": 80.0
}
```

Here, `true` represents present and `false` represents absent.

The JSON file should contain at least five student records.

## 8. Working Principle

The system follows these steps:

1. The user enters an attendance-related command in the terminal.
2. The Python application sends the request to the AI model.
3. The AI model converts the request into a structured JSON action.
4. Python validates the action, student roll number, and date.
5. Python executes the requested attendance operation.
6. Attendance statistics are recalculated.
7. The updated student records are saved to `attendance.json`.
8. The terminal displays the result.

**Important:** The AI model interprets the request, while Python performs the actual calculations and file modifications.

## 9. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Internet connection for AI API requests
- An API key for the selected AI provider
- A terminal or command prompt

### Step 1: Clone or download the project

If the project is hosted on GitHub:

```bash
git clone <your-repository-url>
cd attendance-management
```

Alternatively, create the project folder manually and place the required files inside it.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install dependencies

Create `requirements.txt`:

```text
openai
python-dotenv
```

Install the packages:

```bash
pip install -r requirements.txt
```

### Step 4: Configure the API key

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace the placeholder with your actual API key.

Never upload your API key to a public repository.

### Step 5: Run the application

```bash
python main.py
```

Follow the instructions displayed in the terminal.

## 10. Example Terminal Interaction

The following is an example of the intended interaction.

**Check attendance percentage**

```text
Enter your request:
What is Rahul Sharma's attendance percentage?

Output:
Student: Rahul Sharma
Roll Number: 101
Days Present: 4
Total Days: 5
Attendance Percentage: 80.00%
```

**Check daily attendance**

```text
Enter your request:
Was Rahul present on 10 October 2026?

Output:
Rahul Sharma was absent on 10 October 2026.
```

**Mark attendance**

```text
Enter your request:
Mark Rahul present on 10 October 2026.

Output:
Attendance updated successfully.
Attendance Percentage: 100.00%
```

**Calculate class average**

```text
Enter your request:
Calculate the class attendance average.

Output:
Class Attendance Average: 80.00%
```

*These outputs illustrate the expected behavior; actual results depend on the data stored in `attendance.json`.*

## 11. Attendance Calculation

The attendance percentage of an individual student is calculated using:

Attendance Percentage = (Days Present / Total Attendance Days) × 100

For example, if a student attends four out of five days:

Attendance Percentage = (4 / 5) × 100 = 80%

The class average is calculated using the arithmetic mean of all students' individual attendance percentages.

Class Average = Sum of Individual Attendance Percentages / Number of Students

Python performs these calculations to ensure consistent results.

## 12. Data Validation and Error Handling

The application should validate all AI-generated actions before executing them.

- Verify that the student roll number exists.
- Verify that the date follows the `YYYY-MM-DD` format.
- Ensure the date falls within the configured attendance period.
- Accept only supported attendance actions.
- Ensure the attendance value is a valid Boolean.
- Handle malformed AI responses and API errors.
- Prevent unintended changes when a request is incomplete or ambiguous.
- Recalculate attendance statistics after a successful modification.

For safety, Python—not the AI model—must be responsible for writing changes to the JSON file.

## 13. Security Considerations

- Store API credentials in `.env`.
- Add `.env` and `venv/` to `.gitignore`.
- Do not execute AI-generated Python code.
- Validate AI-generated JSON before using it.
- Keep a backup of attendance records before bulk changes.
- Consider requiring confirmation before modifying attendance records.

## 14. Limitations

- The project requires an internet connection for cloud-based AI requests.
- API usage may incur charges depending on the selected provider.
- JSON storage is suitable for a small demonstration but is not ideal for large, concurrent systems.
- AI interpretation can occasionally be incorrect, so validation is necessary.
- The initial implementation is designed for a small group of students and a limited attendance period.

## 15. Future Enhancements

- Support additional attendance periods and semesters.
- Add CSV and Excel report generation.
- Introduce attendance shortage alerts.
- Add role-based access for teachers and administrators.
- Maintain an audit log of attendance modifications.
- Support offline or locally hosted language models.
- Migrate from JSON to SQLite or PostgreSQL for larger datasets.
- Add a web interface in a future version.

## 16. Conclusion

The AI Attendance Management System demonstrates how Artificial Intelligence can be integrated with Python to simplify attendance management through natural-language commands.

By combining an AI model for request interpretation with deterministic Python calculations, input validation, and JSON file storage, the project provides a simple, understandable, and extensible solution for managing student attendance without requiring a frontend or database.

**Project Type:** AI / Python Mini Project

**Interface:** Command Line / Terminal

**Storage:** JSON File

**Primary Language:** Python

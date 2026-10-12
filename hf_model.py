import os
import json

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Read settings from the .env file
load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
HF_MODEL = os.getenv(
    "HF_MODEL",
    "Qwen/Qwen2.5-7B-Instruct"
)

# Create a Hugging Face client
client = InferenceClient(
    api_key=HF_TOKEN
)

# Instructions given to the AI model
SYSTEM_PROMPT = """
You are an attendance management assistant.

Your job is ONLY to convert the user's request
into a JSON command.

Allowed actions:
- calculate_percentage
- check_attendance
- mark_attendance
- remove_attendance
- class_average

Students:
Rahul Sharma = 101
Priya Singh = 102
Aman Verma = 103
Sneha Gupta = 104
Arjun Kumar = 105

Attendance period:
2026-10-08 to 2026-10-14

Return ONLY valid JSON.

Examples:

User asks for percentage:
{
  "action": "calculate_percentage",
  "roll_no": "101"
}

User asks to check attendance:
{
  "action": "check_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}

User asks to mark attendance:
{
  "action": "mark_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}

User asks to remove attendance:
{
  "action": "remove_attendance",
  "roll_no": "101",
  "date": "2026-10-10"
}

User asks for class average:
{
  "action": "class_average"
}

Do not calculate percentages.
Do not change attendance data.
Only return the JSON command.
"""

def ask_model(user_request):
    if not HF_TOKEN:
        raise ValueError(
            "HF_TOKEN is missing. Check your .env file."
        )

    response = client.chat_completion(
        model=HF_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_request
            }
        ],
        max_tokens=200,
        temperature=0.1
    )

    output = (
        response.choices[0].message.content.strip()
    )

    # Remove Markdown code fences if the model adds them
    if output.startswith("```"):
        output = output.replace("```json", "")
        output = output.replace("```", "")
        output = output.strip()

    # Convert the model's JSON text into a Python dictionary
    return json.loads(output)

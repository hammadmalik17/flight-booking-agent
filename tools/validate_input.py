from typing import Any
import datetime
from crewai.tools import BaseTool

# --- Validators ---
def validate_destination(destination: str) -> bool:
    return bool(destination and destination.strip())

def validate_date(date_str: str) -> bool:
    try:
        flight_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return flight_date > datetime.date.today()
    except ValueError:
        return False

def validate_passenger_name(name: str) -> bool:
    return bool(name and name.replace(" ", "").isalpha())

def validate_all(info: dict) -> dict:
    return {
        "destination": validate_destination(info.get("destination", "")),
        "date": validate_date(info.get("date", "")),
        "passenger_name": validate_passenger_name(info.get("passenger_name", ""))
    }

# --- Custom Tool Class ---
class ValidateUserInputTool(BaseTool):
    name: str = "Validate User Input"
    description: str = "Validates destination, date, and passenger name in user input."

    def _run(self, info: dict) -> Any:
        result = validate_all(info)
        if all(result.values()):
            return "Input is valid."
        errors = [key for key, valid in result.items() if not valid]
        return f"Invalid input for: {', '.join(errors)}"

# --- Instantiated Tool Object ---
validate_user_input_tool_object = ValidateUserInputTool()

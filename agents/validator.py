

from crewai import Agent
from tools.validate_input import validate_user_input_tool_object

validator_agent = Agent(
    role="Flight Input Validator",
    goal="Ensure all user inputs (date, destination, name) are valid before proceeding to booking.",
    backstory="You are a strict and detail-oriented input validation assistant tasked with catching incomplete or malformed flight booking inputs. You help ensure smooth operation by preventing errors early.",
    tools=[validate_user_input_tool_object],
    verbose=True
)

from crewai import Agent
from tools.best_flight_selector import best_flight_selector_tool


planner_agent = Agent(
    role="Flight Planner",
    goal="Select the best available flight based on user's destination and date",
    backstory=(
        "You're a savvy planner who evaluates multiple flights and chooses the most cost-effective one."
    ),
    tools=[best_flight_selector_tool],
    verbose=True
)

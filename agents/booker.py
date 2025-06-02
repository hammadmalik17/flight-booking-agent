from crewai import Agent
from tools.book_flight_tool import book_flight_tool

booker_agent = Agent(
    role="Flight Booker",
    goal="Book the selected flight for the user",
    backstory="You finalize bookings with precision and clarity.",
    tools=[book_flight_tool],
    verbose=True
)

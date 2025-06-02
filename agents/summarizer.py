from crewai import Agent
from tools.summarize_booking_tool import summarize_booking_tool  # ✅ Import the tool wrapper

summarizer_agent = Agent(
    role="Booking Summarizer",
    goal="Provide a friendly summary of the booked flight",
    backstory=(
        "You're a detail-oriented assistant whose job is to clearly summarize the user's booking. "
        "You make sure the final confirmation is easy to understand and pleasant to read."
    ),
    tools=[summarize_booking_tool],  # ✅ Use the tool wrapper
    verbose=True
)
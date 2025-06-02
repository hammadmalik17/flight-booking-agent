

from crewai import Crew, Task, Process
from agents.concierge import concierge_agent
from agents.validator import validator_agent
from agents.planner import planner_agent
from agents.booker import booker_agent
from agents.summarizer import summarizer_agent

from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# --- USER INPUT SECTION (simulate chat with concierge) ---
user_inputs = {
    "destination": "Delhi",
    "date": "2025-06-02",
    "passenger_name": "Tony Stark"
}

# --- TASK DEFINITIONS ---
collect_task = Task(
    description=f"Use the following travel details: destination='{user_inputs['destination']}', date='{user_inputs['date']}', passenger_name='{user_inputs['passenger_name']}'. Return this information as a structured dictionary.",
    expected_output="User travel data as a dictionary with destination, date, and passenger_name",
    agent=concierge_agent
)

validate_task = Task(
    description="Validate the collected user travel data from the previous task.",
    expected_output="Validation results indicating whether the input data is valid",
    agent=validator_agent
)

search_task = Task(
    description="Search for flights using the validated travel info from previous tasks.",
    expected_output="The best available flight option with flight details",
    agent=planner_agent
)

book_task = Task(
    description="Book the selected flight from the search results.",
    expected_output="Booking confirmation and details",
    agent=booker_agent
)

summary_task = Task(
    description="Generate a user-friendly summary of the booked flight.",
    expected_output="Natural language summary of the booking details",
    agent=summarizer_agent
)

# --- CREW ASSEMBLY ---
flight_booking_crew = Crew(
    agents=[
        concierge_agent,
        validator_agent,
        planner_agent,
        booker_agent,
        summarizer_agent
    ],
    tasks=[
        collect_task,
        validate_task,
        search_task,
        book_task,
        summary_task
    ],
    process=Process.sequential,
    verbose=True
)

# --- RUN THE CREW ---
result = flight_booking_crew.kickoff()
print("\n🎫 Final Output:\n", result)
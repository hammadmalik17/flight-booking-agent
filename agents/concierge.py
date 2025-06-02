# # agents/concierge.py

# class ConciergeAgent:
#     def __init__(self):
#         self.user_data = {}

#     def greet_user(self):
#         return "Hello! I'm your flight booking assistant. Where would you like to fly today?"

#     def collect_info(self, info_key, info_value):
#         self.user_data[info_key] = info_value

#     def get_collected_info(self):
#         return self.user_data

#     def is_ready_to_book(self):
#         # Basic check: do we have destination, date, and passenger name?
#         required_fields = ['destination', 'date', 'passenger_name']
#         return all(field in self.user_data for field in required_fields)

#     def summary(self):
#         return f"Booking a flight for {self.user_data.get('passenger_name')} to {self.user_data.get('destination')} on {self.user_data.get('date')}."
from crewai import Agent

# This is the actual agent that CrewAI will use
concierge_agent = Agent(
    role="Flight Booking Concierge",
    goal="Assist users in booking flights by gathering required travel details",
    backstory=(
        "You are the friendly and smart assistant who helps travelers book flights. "
        "Your job is to ask the user for their travel details like destination, date, and name."
    ),
    verbose=True
)

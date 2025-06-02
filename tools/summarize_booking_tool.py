from crewai.tools import BaseTool
from tools.summarize_booking import summarize_booking

class SummarizeBookingTool(BaseTool):
    name: str = "Summarize Booking Tool"
    description: str = "Creates a user-friendly summary of booking details."

    def _run(self, booking_data: dict) -> str:
        return summarize_booking(booking_data)

summarize_booking_tool = SummarizeBookingTool()

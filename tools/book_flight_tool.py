from crewai.tools import BaseTool
from tools.book_flight import book_flight

class BookFlightTool(BaseTool):
    name: str = "Book Flight Tool"
    description: str = "Books a flight for a user given flight and user details."

    def _run(self, input_data: dict) -> dict:
        return book_flight(input_data)

book_flight_tool = BookFlightTool()
from crewai.tools import BaseTool
from tools.search_flights import search_flights  # keep your import consistent

class BestFlightSelectorTool(BaseTool):
    name: str = "Best Flight Selector"
    description: str = "Selects the cheapest flight for a given destination and date."

    def _run(self, input_data: dict) -> dict:
        destination = input_data.get("destination")
        date = input_data.get("date")

        flights = search_flights(destination, date)
        if not flights:
            return {"message": "No valid flights found."}

        best_flight = sorted(flights, key=lambda x: x["price"])[0]
        return best_flight

best_flight_selector_tool = BestFlightSelectorTool()

import random
from datetime import datetime

def search_flights(destination: str, date: str) -> list:
    try:
        # Check if date is valid
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return []

    airlines = ["IndiGo", "Air India", "SpiceJet", "Vistara", "Akasa Air"]
    flights = []

    for i in range(3):  # generate 3 fake flights
        flight = {
            "flight_number": f"{random.choice(['AI', '6E', 'SG', 'UK', 'QP'])}{random.randint(100, 999)}",
            "airline": random.choice(airlines),
            "destination": destination.title(),
            "date": date,
            "price": random.randint(3000, 9000),
        }
        flights.append(flight)

    return flights

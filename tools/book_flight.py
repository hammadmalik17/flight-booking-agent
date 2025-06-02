import json
import os

BOOKINGS_FILE = "data/bookings.json"

def book_flight(input_data):
    """
    Book a flight with the provided input data.
    input_data should contain both flight and user information.
    """
    # Handle both dict input and separate parameters for flexibility
    if isinstance(input_data, dict):
        # Extract flight and user info from the input data
        flight = input_data.get("flight", input_data)
        user_info = input_data.get("user", {
            "name": input_data.get("passenger_name", "Unknown"),
            "email": f"{input_data.get('passenger_name', 'user').lower().replace(' ', '.')}@example.com"
        })
    else:
        # Fallback for direct parameters (your original structure)
        flight = input_data
        user_info = {"name": "Unknown", "email": "user@example.com"}
    
    # Combine flight and user info into one booking record
    booking = {
        "user": user_info,
        "flight": flight,
    }

    # Load existing bookings
    if os.path.exists(BOOKINGS_FILE):
        with open(BOOKINGS_FILE, "r") as file:
            bookings = json.load(file)
    else:
        bookings = []

    # Add new booking
    bookings.append(booking)

    # Save updated bookings
    with open(BOOKINGS_FILE, "w") as file:
        json.dump(bookings, file, indent=2)

    # Return confirmation message
    return {
        "message": "Flight successfully booked!",
        "booking_details": booking
    }
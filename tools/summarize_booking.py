

def summarize_booking(booking: dict) -> str:
    user = booking.get("user", {})
    flight = booking.get("flight", {})

    return (
        f"Booking Confirmation for {user.get('name')} ({user.get('email')}):\n"
        f"- Flight Number: {flight.get('flight_number')}\n"
        f"- Airline: {flight.get('airline')}\n"
        f"- Destination: {flight.get('destination')}\n"
        f"- Date: {flight.get('date')}\n"
        f"- Price: ₹{flight.get('price')}\n"
        f"Thank you for booking with us!"
    )





# Room Management with JSON Storage

import json
import os

ROOM_FILE = "rooms.json"

rooms = {}


# Load previously saved rooms
def load_rooms():

    global rooms

    if os.path.exists(ROOM_FILE):

        try:
            with open(ROOM_FILE, "r") as file:
                rooms = json.load(file)

        except (json.JSONDecodeError, OSError):
            rooms = {}

    else:
        rooms = {}


# Save rooms permanently
def save_rooms():

    with open(ROOM_FILE, "w") as file:
        json.dump(rooms, file, indent=4)


# Add a new examination room
def add_room():

    room_number = input("Enter Room Number: ").strip()

    if not room_number:
        print("Room number cannot be empty!")
        return

    if room_number in rooms:
        print("Room already exists!")
        return

    try:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))

        if rows <= 0 or columns <= 0:
            print("Rows and columns must be positive!")
            return

    except ValueError:
        print("Please enter valid numbers!")
        return

    seats = [
        [None for _ in range(columns)]
        for _ in range(rows)
    ]

    rooms[room_number] = {
        "rows": rows,
        "columns": columns,
        "seats": seats
    }

    save_rooms()

    print("Room added and saved successfully!")


# Display available rooms
def view_rooms():

    if not rooms:
        print("No rooms available.")
        return

    print("\n----- AVAILABLE ROOMS -----")

    for room_number, details in rooms.items():

        print(f"\nRoom Number: {room_number}")
        print(f"Rows: {details['rows']}")
        print(f"Columns: {details['columns']}")
        print(f"Total Seats: {details['rows'] * details['columns']}")

    print("---------------------------")


# Load rooms when the module is imported
load_rooms()

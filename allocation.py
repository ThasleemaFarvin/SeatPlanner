
# Constraint-Based Seat Allocation using Backtracking

from students import students
from rooms import rooms, save_rooms


def allocate_seats():

    # Check student availability
    if not students:
        print("\nNo students available!")
        return

    # Check room availability
    if not rooms:
        print("\nNo examination rooms available!")
        return

    # Display available rooms
    print("\n========== AVAILABLE ROOMS ==========")

    for room_no, details in rooms.items():
        capacity = details["rows"] * details["columns"]

        print(
            f"Room {room_no} - "
            f"Rows: {details['rows']}, "
            f"Columns: {details['columns']}, "
            f"Capacity: {capacity}"
        )

    print("=====================================")

    # Select rooms
    selected_input = input(
        "\nEnter room numbers separated by commas: "
    )

    selected_rooms = [
        room.strip()
        for room in selected_input.split(",")
        if room.strip()
    ]

    # Validate room selection
    if not selected_rooms:
        print("Please select at least one room!")
        return

    if len(selected_rooms) != len(set(selected_rooms)):
        print("Duplicate room selection!")
        return

    for room_no in selected_rooms:
        if room_no not in rooms:
            print(f"Room {room_no} does not exist!")
            return

    # Calculate total available seats
    total_seats = sum(
        rooms[room_no]["rows"] * rooms[room_no]["columns"]
        for room_no in selected_rooms
    )

    if len(students) > total_seats:
        print("\nNot enough seats in the selected rooms!")
        print("Required seats:", len(students))
        print("Available seats:", total_seats)
        return

    # Create temporary seating arrangements
    temp_rooms = {}

    for room_no in selected_rooms:
        details = rooms[room_no]

        temp_rooms[room_no] = [
            [None for _ in range(details["columns"])]
            for _ in range(details["rows"])
        ]

    # Prepare student list
    student_list = list(students.items())

    # Sort students by branch
    student_list.sort(key=lambda x: x[1]["branch"])

    # Store all available seat positions
    seat_positions = []

    for room_no in selected_rooms:
        details = rooms[room_no]

        for row in range(details["rows"]):
            for col in range(details["columns"]):
                seat_positions.append((room_no, row, col))

    # Check seating constraints
    def is_valid(room_no, row, col, branch):

        seat_map = temp_rooms[room_no]

        # Check LEFT
        if col > 0:
            left = seat_map[row][col - 1]

            if left is not None and left["branch"] == branch:
                return False

        # Check RIGHT
        if col < len(seat_map[row]) - 1:
            right = seat_map[row][col + 1]

            if right is not None and right["branch"] == branch:
                return False

        # Check FRONT
        if row > 0:
            front = seat_map[row - 1][col]

            if front is not None and front["branch"] == branch:
                return False

        # Check BEHIND
        if row < len(seat_map) - 1:
            behind = seat_map[row + 1][col]

            if behind is not None and behind["branch"] == branch:
                return False

        return True

    # Backtracking algorithm
    def backtrack(index):

        if index == len(student_list):
            return True

        reg_no, student = student_list[index]
        branch = student["branch"]

        for room_no, row, col in seat_positions:

            if temp_rooms[room_no][row][col] is not None:
                continue

            if is_valid(room_no, row, col, branch):

                # Place student
                temp_rooms[room_no][row][col] = {
                    "reg_no": reg_no,
                    "name": student["name"],
                    "branch": branch
                }

                if backtrack(index + 1):
                    return True

                # Undo placement
                temp_rooms[room_no][row][col] = None

        return False

    # Start allocation
    print("\nAllocating seats...")

    if backtrack(0):

        # Clear previous allocations from all rooms
        for room_no, details in rooms.items():

            rows = details["rows"]
            columns = details["columns"]

            rooms[room_no]["seats"] = [
                [None for _ in range(columns)]
                for _ in range(rows)
            ]

        # Save new allocation
        for room_no in selected_rooms:
            rooms[room_no]["seats"] = temp_rooms[room_no]

        save_rooms()

        print("\n=====================================")
        print("SEAT ALLOCATION COMPLETED SUCCESSFULLY!")
        print("=====================================")
        print("Students Allocated:", len(students))
        print("Rooms Used:", ", ".join(selected_rooms))
        print("Total Available Seats:", total_seats)

    else:
        print("\nNo valid seating arrangement found.")
        print("Please check the branch distribution")
        print("and selected room configurations.")

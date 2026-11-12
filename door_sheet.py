
# Door Sheet Generation

from rooms import rooms


def generate_door_sheet():

    if not rooms:
        print("\nNo examination rooms available!")
        return

    print("\n==============================================")
    print("              EXAMINATION DOOR SHEET")
    print("==============================================")

    found_allocation = False

    for room_no, details in rooms.items():

        seats = details.get("seats", [])

        # Collect allocated students
        room_students = []

        for row_index, row in enumerate(seats):

            for col_index, seat in enumerate(row):

                if seat is not None:
                    room_students.append({
                        "reg_no": seat["reg_no"],
                        "name": seat["name"],
                        "branch": seat["branch"],
                        "row": row_index + 1,
                        "column": col_index + 1
                    })

        if not room_students:
            continue

        found_allocation = True

        # Sort students by register number
        room_students.sort(key=lambda x: x["reg_no"])

        print(f"\nROOM NUMBER: {room_no}")
        print("-" * 55)

        print(
            f"{'Register No.':<18}"
            f"{'Name':<18}"
            f"{'Branch':<10}"
            f"{'Seat':<8}"
        )

        print("-" * 55)

        for student in room_students:

            seat_position = (
                f"R{student['row']}-C{student['column']}"
            )

            print(
                f"{student['reg_no']:<18}"
                f"{student['name']:<18}"
                f"{student['branch']:<10}"
                f"{seat_position:<8}"
            )

        print("-" * 55)
        print("Total Students:", len(room_students))

    if not found_allocation:
        print("\nNo seating allocation found!")

    print("\n==============================================")
    print("           END OF DOOR SHEET")
    print("==============================================")

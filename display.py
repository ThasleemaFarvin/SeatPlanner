
# Display Room-wise Seating Arrangement

from rooms import rooms


def display_seating():

    if not rooms:
        print("No examination rooms available!")
        return

    for room_no, details in rooms.items():

        print("\n")
        print("=" * 65)
        print(f"              ROOM NUMBER: {room_no}")
        print("=" * 65)

        seats = details["seats"]

        if all(student is None for row in seats for student in row):
            print("No seating allocation found for this room.")
            continue

        print("\n")

        for row_index, row in enumerate(seats):

            print(f"Row {row_index + 1}:")

            for student in row:

                if student is None:
                    print(f"{'EMPTY':^20}", end=" ")
                else:
                    print(
                        f"{student['reg_no']} ({student['branch']})".center(20),
                        end=" "
                    )

            print("\n")

        print("=" * 65)

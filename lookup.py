
# Student Lookup

from students import students
from rooms import rooms


def search_student():

    if not students:
        print("\nNo student records available!")
        return

    reg_no = input("\nEnter Student Register Number: ").strip()

    # Check whether student exists
    if reg_no not in students:
        print("\nStudent not found!")
        return

    student = students[reg_no]

    # Search for the student's allocated seat
    for room_no, details in rooms.items():

        seats = details.get("seats", [])

        for row_index, row in enumerate(seats):

            for col_index, seat in enumerate(row):

                if seat is not None and seat.get("reg_no") == reg_no:

                    print("\n========== STUDENT DETAILS ==========")
                    print("Register Number:", reg_no)
                    print("Student Name:", student["name"])
                    print("Branch:", student["branch"])
                    print("Room Number:", room_no)
                    print("Row Number:", row_index + 1)
                    print("Column Number:", col_index + 1)
                    print("=====================================")

                    return

    # Student exists but has no seat allocation
    print("\nStudent is registered but seat is not allocated yet.")

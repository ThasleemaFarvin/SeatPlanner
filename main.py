
from rooms import add_room, view_rooms
from students import add_students, view_students
from allocation import allocate_seats
from display import display_seating
from lookup import search_student
from door_sheet import generate_door_sheet


while True:

    print("\n========== SEAT PLANNER ==========")
    print("1. Add Examination Room")
    print("2. View Available Rooms")
    print("3. Add Students")
    print("4. Allocate Seats")
    print("5. View Seating Arrangement")
    print("6. Search Student")
    print("7. View Student List")
    print("8. Generate Door Sheet")
    print("9. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_room()

    elif choice == "2":
        view_rooms()

    elif choice == "3":
        add_students()

    elif choice == "4":
        allocate_seats()

    elif choice == "5":
        display_seating()

    elif choice == "6":
        search_student()

    elif choice == "7":
        view_students()

    elif choice == "8":
        generate_door_sheet()

    elif choice == "9":
        print("Thank you for using SeatPlanner!")
        break

    else:
        print("Invalid choice! Please try again.")

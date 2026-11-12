
# Student Management with JSON Storage

import json
import os

STUDENT_FILE = "students.json"

students = {}


# Load previously saved students
def load_students():

    if os.path.exists(STUDENT_FILE):

        try:
            with open(STUDENT_FILE, "r") as file:
                data = json.load(file)

            students.clear()
            students.update(data)

        except (json.JSONDecodeError, OSError):
            print("Warning: Could not load student records.")


# Save students permanently
def save_students():

    with open(STUDENT_FILE, "w") as file:
        json.dump(students, file, indent=4)


# Add students
def add_students():

    try:
        count = int(input("Enter number of students to add: "))

        if count <= 0:
            print("Enter a valid number of students.")
            return

        added = 0

        for i in range(count):

            print(f"\nEnter details of Student {i + 1}")

            reg_no = input("Register Number: ").strip()

            if not reg_no:
                print("Register number cannot be empty!")
                continue

            if reg_no in students:
                print("Student already exists!")
                continue

            name = input("Student Name: ").strip()
            branch = input("Branch: ").strip().upper()

            if not name or not branch:
                print("Name and branch cannot be empty!")
                continue

            students[reg_no] = {
                "name": name,
                "branch": branch
            }

            added += 1

        if added > 0:
            save_students()
            print(f"\n{added} student(s) added and saved successfully!")

        else:
            print("No new students were added.")

    except ValueError:
        print("Please enter a valid number.")


# Display all students
def view_students():

    if not students:
        print("No students available.")
        return

    print("\n========== STUDENT LIST ==========")

    for reg_no, details in students.items():

        print("\nRegister Number:", reg_no)
        print("Name:", details["name"])
        print("Branch:", details["branch"])
        print("----------------------------------")


# Load students automatically
load_students()
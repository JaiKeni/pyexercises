"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""


# 1. In:
# The program asks the user to enter their first name, last name,
# email address and student number.

# 2. Process:
# The program collects the information using input().
# It removes extra spaces using strip().
# It then saves the information in a CSV file using csv.writer().

# 3. Out:
# The output file is called 7.0_student_data.csv.
# It contains four columns: first_name, last_name, email
# and student_number.

# 4. Why these columns, and what would I do with 200 rows?
# I chose these columns to keep a record of student information.
# With 200 rows, I could organise student records, search for
# students and identify them using their student numbers.


import csv
import os

print("Please fill in the following details:")

first_name = input("First Name: ").strip()
last_name = input("Last Name: ").strip()
email = input("Email: ").strip()
student_number = input("Student Number: ").strip()

filename = "7.0_student_data.csv"

file_exists = os.path.exists(filename)

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")

    if not file_exists or os.path.getsize(filename) == 0:
        writer.writerow(["first_name", "last_name", "email", "student_number"])

    writer.writerow([first_name, last_name, email, student_number])

print("Student information saved successfully!")


# MY COMMENTS:
# I used append mode so that new student details are added
# without deleting the previous entries.
# The header is written only when the file is new or empty.
# I used semicolons to match the format of my CSV file.
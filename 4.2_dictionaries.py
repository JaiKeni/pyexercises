"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. The reservation is written inside the program as a dictionary.
# 2. Process: I read one field, change one field, remove one field, then go through the dictionary and print every field with its value.
# 3. Out: One field, the changed dictionary, the dictionary after removing a field, then every field with its value. Also a safe message for a field that does not exist.
# 4. My object, my five fields, and why those:
#    Object: a table reservation at a restaurant.
#    name: so the staff know whose reservation it is.
#    guests: so they prepare a table of the right size.
#    time: so they know when the table must be ready.
#    phone: so they can call if something changes.
#    notes: so they remember allergies or special requests.


# Your code below
reservation = {
    "name": "Anna",
    "guests": 4,
    "time": "19:30",
    "phone": "0612345678",
    "notes": "one guest is allergic to nuts"
}

# Read one field
print("The name is:", reservation["name"])

# Change one field
reservation["guests"] = 5
print("After the change:", reservation)

# Remove one field
del reservation["notes"]
print("After removing notes:", reservation)

# Show every field with its value
for field in reservation:
    print(field, ":", reservation[field])

# Ask for a field that does not exist (safe way)
print("The email is:", reservation.get("email", "no email saved"))

#My Comments 
# CHECK: First I wrote print(reservation["email"]).
# The program crashed with a KeyError, because "email" is not in the dictionary.
# To fix it, I used .get("email", "no email saved"). Now the program shows
# "no email saved" and does not crash.
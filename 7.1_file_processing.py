"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""


# WHAT IS WRONG WITH names.txt?
# 1. There are two empty lines in the file.
# 2. Some names have extra spaces at the beginning.
# 3. First names have inconsistent capitalisation.
# 4. Last names have inconsistent capitalisation.
# 5. Guido van Rossum has a two-word surname.

# 1. In:
# The program reads names from names.txt.

# 2. Process, problem by problem:
# Empty lines are removed.
# Extra spaces are removed using strip().
# First names are changed to start with a capital letter.
# Last names are also cleaned and capitalised.
# The surname "van Rossum" is kept together.
# The names are sorted alphabetically by last name.

# 3. Out:
# The program creates a new file called sorted_names.txt.
# It contains the cleaned names sorted by last name.

# 4. How I decide which word is the last name:
# The first word is the first name and all the remaining
# words are considered the last name.
# This also works for Guido van Rossum.


# Load the names from the original file
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Create an empty list for the cleaned names
cleaned_names = []

# Clean each line
for line in lines:

    # Remove extra spaces
    name = line.strip()

    # Skip empty lines
    if name == "":
        continue

    # Separate the first name and last name
    parts = name.split()

    first_name = parts[0].capitalize()

    # Keep all remaining words together as the surname
    last_name = " ".join(parts[1:])

    # Capitalise the surname correctly
    if last_name.lower().startswith("van "):
        last_name = "van " + last_name[4:].capitalize()
    else:
        last_name = last_name.title()

    # Combine first name and last name
    full_name = first_name + " " + last_name

    # Add the cleaned name to the list
    cleaned_names.append(full_name)


# Sort names alphabetically by last name
sorted_names = sorted(
    cleaned_names,
    key=lambda name: " ".join(name.split()[1:]).lower()
)


# Save the sorted names in a new file
with open("sorted_names.txt", "w", encoding="utf-8") as file:
    for name in sorted_names:
        file.write(name + "\n")


print("Names cleaned and sorted successfully!")
print("Total names saved:", len(sorted_names))


# MY COMMENTS:
# I removed the empty lines and extra spaces.
# I sorted the names using their last names.
# I saved the result in a new file so the original
# names.txt file remains unchanged.

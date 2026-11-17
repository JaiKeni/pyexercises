"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# ANSWERS:
# 1. What goes in?
# Two values: zero (0) and an empty string ("").

# 2. What happens to it?
# Python performs comparison operators and logical operations
# between the two values and displays the results in a table.

# 3. What comes out?
# A readable table showing whether each comparison and
# logical combination is True or False.

# 4. Which two values did you pick, and which comparison result surprised you?
# I picked 0 and an empty string ("").
# I was surprised that 0 == "" returns False because
# both represent an absence of value, but they have different types.


# PREDICTIONS BEFORE RUNNING:
# 0 == ""       False
# 0 != ""       True
# 0 < ""        TypeError
# 0 > ""        TypeError
# 0 <= ""       TypeError
# 0 >= ""       TypeError
# True and False = False
# True or False  = True
# not True       = False


# INPUT: Two values
a = 0
b = ""

# COMPARISONS
equal = (a == b)
not_equal = (a != b)

# LOGICAL COMBINATIONS
logical_and = equal and not_equal
logical_or = equal or not_equal
logical_not = not equal

# OUTPUT: Readable table
print("OPERATORS COMPARISON TABLE")
print("-" * 45)
print(f"{'Operation':<25} {'Result':<15}")
print("-" * 45)

print(f"{'a == b':<25} {equal}")
print(f"{'a != b':<25} {not_equal}")
print(f"{'equal and not_equal':<25} {logical_and}")
print(f"{'equal or not_equal':<25} {logical_or}")
print(f"{'not equal':<25} {logical_not}")

print("-" * 45)

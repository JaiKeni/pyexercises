"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The program receives a number entered by the user.
# 2. Process:
#    First, is_positive() checks if the number is greater than zero.
#    Second, is_negative() checks if the number is less than zero.
#    Third, is_zero() checks if the number is equal to zero.
#    Finally, detailed_message() uses these three functions to
#    decide whether the number is positive, negative or zero.
# 3. Out: The program returns a message explaining the result.

# 4. Question: Is the number positive, negative or zero?
#    Splitting the program into three small functions makes it
#    easier to test each condition separately and find mistakes.


# FUNCTION 1: Check if the number is positive
def is_positive(num):
    return num > 0


# FUNCTION 2: Check if the number is negative
def is_negative(num):
    return num < 0


# FUNCTION 3: Check if the number is zero
def is_zero(num):
    return num == 0


# TEST EACH SMALL FUNCTION BEFORE COMBINING THEM

# Test 1: Input = 5, Expected output = True
print("Test positive:", is_positive(5))

# Test 2: Input = -4, Expected output = True
print("Test negative:", is_negative(-4))

# Test 3: Input = 0, Expected output = True
print("Test zero:", is_zero(0))


# FUNCTION 4: Use the three functions to give a detailed message
def detailed_message(num):
    if is_positive(num):
        return "The number is positive."
    elif is_negative(num):
        return "The number is negative."
    elif is_zero(num):
        return "The number is zero."


# CALL THE FOURTH FUNCTION
number = int(input("Enter a number: "))
print(detailed_message(number))


# My Comments: 
# I tested the three functions separately with 5, -4 and 0.
# All three gave the expected output.
# The fourth function combines them to identify the number.
# Splitting the code makes it easier to understand and check for mistakes.
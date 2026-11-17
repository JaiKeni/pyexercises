"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""


# Name: Jai Ajay Keni
# Exercise 9.0 — Surviving what you did not expect

# 1. In:
# The user enters a value using the keyboard.

# 2. Process:
# Python converts the input into a number and divides 100 by it.

# 3. Out:
# The result of the division or an error message if the input is invalid.

# 4. The two failures:
# ZeroDivisionError happens when the user enters 0.
# ValueError happens when the user enters text like "abc".
# They should have different messages because the problems are different.

# Catching each error separately is better because we can give
# the user a specific message explaining what went wrong.

# CHECK YOURSELF:
# 1. Entering 10 gives 10.0.
# 2. Entering 0 displays a division by zero message.
# 3. Entering abc displays an invalid number message.
# 4. Entering an empty line displays an invalid number message.


# Your code below

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    user_input = input("Enter a number to divide 100 by: ")

    try:
        number = float(user_input)

        result = 100 / number

        print("Result:", result)
        break

    except ValueError:
        print("Invalid input! Please enter a valid number.")

    except ZeroDivisionError:
        print("You cannot divide by zero! Please enter another number.")

    attempts += 1

else:
    print("Maximum attempts reached. Please try again later.")

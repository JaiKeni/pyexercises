"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: One whole number N typed by the user.
# 2. Process: The number is changed from text to a number with int(). Then I go through 1 to N and check each number with % 2.
# 3. Out: One line for each number from 1 to N, saying if it is odd or even.
# 4. What happens on 0, on a negative number, on a very large number:
#    0: The program says N must be at least 1 and stops, because there is nothing to count.
#    Negative number: Same message as 0, because there is no list from 1 to a negative number.
#    Very large number (like 5000): The program says the number is too big and stops. My limit is 100, so the screen is not flooded.


# Your code below
N = int(input("Enter a number: "))

if N < 1:
    print("The number must be at least 1.")
elif N > 100:
    print("The number is too big. Please use 100 or less.")
else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")

#My comments: 
# CHECK 1: I ran it with 6.
# I saw 3 odd numbers (1, 3, 5) and 3 even numbers (2, 4, 6). I counted them and it is correct.

# CHECK 2: I ran it with my three edge cases.
# 0: The program showed "The number must be at least 1." and stopped.
# -4: The program showed "The number must be at least 1." and stopped.
# 5000: The program showed "The number is too big. Please use 100 or less." and stopped.
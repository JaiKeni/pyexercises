"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Words typed by the user, one answer each time the program asks.
# 2. Process: The program asks "Do you confirm the reservation? (yes/no)" in a while loop. Each answer is cleaned with strip() and lower(), so "Yes", "yes" and " yes " are the same. I count the attempts and keep every answer in a list.
# 3. Out: A message saying if the user confirmed or ran out of attempts, then a summary.
# 4. My stop condition, my attempt limit, my summary:
#    Stop condition: the user types "yes" (capitals and spaces do not matter).
#    Attempt limit: 3. After 3 wrong answers the program stops by itself, so it can never run for ever.
#    Summary: the number of attempts and the list of answers the user typed.


# Your code below
max_attempts = 3
attempts = 0
answers = []
confirmed = False

while attempts < max_attempts and not confirmed:
    answer = input("Do you confirm the reservation? (yes/no): ")
    attempts = attempts + 1
    answers.append(answer)

    if answer.strip().lower() == "yes":
        confirmed = True
    else:
        print("Not confirmed, try again.")

if confirmed:
    print("Reservation confirmed.")
else:
    print("Too many attempts. Reservation cancelled.")

print("Summary: attempts used:", attempts)
print("Summary: answers typed:", answers)

#My Comments: 
# CHECK 1: I ran it and never typed "yes" (I typed "no", "abc", "maybe").
# The program stopped after 3 attempts and showed "Too many attempts". It did not run for ever.

# CHECK 2: I ran it and typed "  YES  " (capitals and extra spaces).
# The program accepted it as "yes" and stopped after 1 attempt.
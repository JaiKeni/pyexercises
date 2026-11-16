"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The function receives a list of monthly restaurant sales in euros.
# 2. Process: The function adds all the sales values using sum().
# 3. Out: The function returns the total sales in euros.
# 4. Function name: calculate_total_sales.
#    Its name clearly explains what the function does.

# The function uses return instead of print because return gives the
# result back to the program so it can be reused in calculations.
# print only displays the result on the screen.

# CHECK: When the function receives an empty list, it returns 0.
# This is acceptable because there are no sales to add.

# MY COMMENTS / CHECK:
# I checked the first three months by hand:
# 4200 + 3800 + 5100 = 13100.
# The program also gives 13100, so the result is correct.
# The total sales for all eight months are 37600 euros.


def calculate_total_sales(sales):
    total = sum(sales)
    return total


# Monthly restaurant sales from Exercise 4.0
monthly_sales = [4200, 3800, 5100, 4700, 6000, 5500, 3900, 4400]

# Call the function three times with different inputs

result1 = calculate_total_sales(monthly_sales[:3])
print("Total sales for the first three months:", result1)

result2 = calculate_total_sales(monthly_sales[:5])
print("Total sales for the first five months:", result2)

result3 = calculate_total_sales(monthly_sales)
print("Total sales for all eight months:", result3)

empty_result = calculate_total_sales([])
print("Total sales for an empty list:", empty_result)

"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. The list is written inside the program.
# 2. Process: The program prints the list, picks one item, sorts a copy of the list, and adds up all the values with sum().
# 3. Out: The whole list, one item, the sorted list, and the total sales.
# 4. What my list is about, and what I computed from it:
#    My list is the monthly sales of a restaurant in euros (8 months).
#    I computed the total. It is interesting because it shows how much money the restaurant made in all.


# Your code below
monthly_sales = [4200, 3800, 5100, 4700, 6000, 5500, 3900, 4400]

print("The whole list is:", monthly_sales)
print("The first month's sales are:", monthly_sales[0])

sorted_sales = sorted(monthly_sales)
print("The sorted list is:", sorted_sales)

total = sum(monthly_sales)
print("The total sales are:", total)

# My Comments: 
# CHECK: I worked out by hand the first three items: 4200 + 3800 + 5100 = 13100.
# I ran sum(monthly_sales[:3]) and my program also gave 13100, so it agrees.
# For the full list, the total is 37600.
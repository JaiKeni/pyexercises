"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. The list is the monthly sales list copied from exercise 4.0.
# 2. Process: I add up the total with sum(). Then I go through the list with a for loop and enumerate(), and for each item I calculate its share of the total.
# 3. Out: One line for each month with its position, its sales and its share of the total sales in percent.
# 4. What I compute for each item, and why it is worth showing:
#    I compute the share of the total (sales / total * 100).
#    The reader sees which months bring the most money, so it is easier to compare them than with the raw numbers.


# Your code below
monthly_sales = [4200, 3800, 5100, 4700, 6000, 5500, 3900, 4400]

total = sum(monthly_sales)

for position, sales in enumerate(monthly_sales, start=1):
    share = sales / total * 100
    print("Month", position, ": sales", sales, "euros, that is", round(share, 1), "% of the total")


# CHECK: My list has 8 items and my program printed 8 lines, so there is no off-by-one.
# I used enumerate(..., start=1) so the positions go from 1 to 8 and not from 0 to 7.

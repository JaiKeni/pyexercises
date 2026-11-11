"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Nothing typed by the user. The list is the monthly sales list from exercise 4.0.
# 2. Process: I make four reordered versions of the list. Some ways change the list itself, others make a new list. I only use the ways that leave the original safe.
# 3. Out: The four ordered lists, then the original list at the end to prove it did not change.
# 4. My four orders, and which ones modify the original:
#    1) sorted(list): smallest to biggest. Makes a NEW list, original is not changed.
#    2) sorted(list, reverse=True): biggest to smallest. Makes a NEW list, original is not changed.
#    3) list[::-1]: reversed order. Makes a NEW list, original is not changed.
#    4) copy then .sort(): I copy the list with .copy() first, then use .sort() on the copy. .sort() changes the list it is used on, but here it is the copy, so the original is safe.
#    Without the copy, .sort() and .reverse() would modify the original.


# Your code below
monthly_sales = [4200, 3800, 5100, 4700, 6000, 5500, 3900, 4400]

print("Smallest to biggest:", sorted(monthly_sales))
print("Biggest to smallest:", sorted(monthly_sales, reverse=True))
print("Reversed order:", monthly_sales[::-1])

sales_copy = monthly_sales.copy()
sales_copy.sort()
print("Sorted copy with .sort():", sales_copy)

print("Original list:", monthly_sales)

#My Comments:
# CHECK: The original list shows [4200, 3800, 5100, 4700, 6000, 5500, 3900, 4400].
# I compared it with 4.0 item by item and it is the same, so the original was not damaged.
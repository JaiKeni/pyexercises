"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Two whole numbers typed by the user.
# 2. Process: The inputs are changed from text to numbers with int(), then I add, subtract, multiply and divide them.
# 3. Out: The two numbers, then the sum, difference, product and quotient.
# 4. What happens when the second number is zero, and why: If the second number is zero: The program shows a message instead of dividing, because dividing by zero crashes Python.


# Your code below
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

print(" The first number is : ", number_1)
print(" The second number is : ", number_2)

#sum of two number
sum = number_1 + number_2
print("The sum of two numbers is ",sum)

#difference of two numbers
diff = number_1 - number_2
print("the diff of two numbers is: ",diff)

#product of two numbers
product = number_1 * number_2
print("The product is:", product)

print("The product is:", product)
if number_2 == 0:
    print("The quotient cannot be calculated: division by zero is impossible.")
else:
    quotient = number_1 / number_2
    print("The quotient is:", quotient)

# My Comments
# CHECK 1: I ran it with 7 and 2.
# In my head, 7 / 2 = 3.5.
# My program shows 3.5, because "/" gives a decimal number.
# If it showed 3, it would mean I used "//", which cuts off the decimal part.

# CHECK 2: I ran it with 7 and 0.
# The sum, difference and product work normally.
# For the division, my program shows a message instead of crashing.

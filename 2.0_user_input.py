"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Name of the person and the number guests they're bringing
# 2. Process: both name and number variables are defined and then both are commanded to print and at last a sentence combining both name and number is asked to print
# 3. Out:  Three lines on screen: "My name is ...", "Number of guests ...", and a sentence like "...has reserved table for them and... others".
# 4. My two fields, and what I would do with them: Get persons name and expected guests theyre bringing to reserve a table for them all


# Your code below
name = input("Enter your name: ")
number = input("Enter number of guests your bringing: ")

print("My name is ", name )
print("Number of guests ", number )

print(name + " has reserved table for themself and " + number + " others")

# Comments 
# when line was empty : No crash. Sentence printed with a blank gap where the number should be.
# when space was typed :  Looks the same as empty, but it is a string containing one space.
# when input was random: Printed "abc others", because nothing checks or converts the input.
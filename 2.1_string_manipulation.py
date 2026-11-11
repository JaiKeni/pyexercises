"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: One sentence typed by the user.
# 2. Process: The sentence is stored as text, then four string methods are applied to it without changing the original.
# 3. Out: Four lines on screen, one per transformation.
# 4. My four transformations, and when each is useful: stripped - removes spaces at both ends.
#    upper()   -> ALL CAPITALS: making a title or warning stand out.
#    title()   -> Each Word Capitalized: formatting a person's or a product's name.
#    replace() -> swaps one text for another: changing " " to "_" to make a file name.
# Type a sentence: Welcome back!, Stripped: Welcome back!, Upper: WELCOME BACK!, Title: Welcome Back!, File name style: Welcome_back!


# Your code below
sentence = input("Type a sentence: ")

print("Stripped:", sentence.strip())
print("Upper:", sentence.upper())
print("Title:", sentence.title())
print("File name style:", sentence.strip().replace(" ", "_"))

# My Comments
# test sentence: "Welcome back!"
# strip():   "Welcome back!"   -> as expected: nothing to remove, no spaces at the ends.
# upper():   "WELCOME BACK!"   -> as expected: all capitals, the "!" is unchanged.
# title():   "Welcome Back!"   -> as expected: each word capitalized, so "back" became "Back".
# replace(): "Welcome_back!"   -> as expected: the space became "_", the capital W stayed.
"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below

# Name: Jai Ajay Keni
# Exercise 10.0 — Checking the shape of text

# ANSWERS:

# 1. What goes in?
# The user enters a campaign name, brand email and campaign budget.

# 2. What happens to it?
# Python checks each input against specific validation rules.
# All three fields must be valid before the information is saved.

# 3. What comes out?
# If all three inputs are valid, the campaign information is saved
# and displayed. Otherwise, error messages are displayed.

# 4. My three fields and their rules:
#
# Campaign name:
# - Must contain between 3 and 30 characters.
# - Can contain letters, numbers and spaces.
# - Cannot be empty.
#
# Brand email:
# - Must contain text before and after @.
# - Must end with a dot followed by at least two letters.
# - No spaces are allowed.
#
# Campaign budget:
# - Must be a positive whole number.
# - Cannot be zero or negative.

# REGULAR EXPRESSION EXPLANATION:
#
# Campaign name pattern: ^[A-Za-z0-9 ]{3,30}$
# ^ means the beginning of the text.
# [A-Za-z0-9 ] allows letters, numbers and spaces.
# {3,30} means between 3 and 30 characters.
# $ means the end of the text.
#
# Email pattern: ^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$
# ^ means the beginning of the text.
# [^@\s]+ means one or more characters except @ and spaces.
# @ means the email must contain an @ symbol.
# \. means a dot.
# [A-Za-z]{2,} means at least two letters after the dot.
# $ means the end of the text.


import re

# INPUT
campaign_name = input("Enter campaign name: ")
brand_email = input("Enter brand email: ")
budget = input("Enter campaign budget: ")

# VALIDATION
name_valid = re.fullmatch(r"[A-Za-z0-9 ]{3,30}", campaign_name)

email_valid = re.fullmatch(
    r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}", brand_email
)

try:
    budget_number = int(budget)
    budget_valid = budget_number > 0
except ValueError:
    budget_valid = False

# CHECK ALL THREE FIELDS
if name_valid and email_valid and budget_valid:

    # SAVE ONLY IF EVERYTHING IS VALID
    campaign = {
        "Campaign Name": campaign_name,
        "Brand Email": brand_email,
        "Campaign Budget": budget_number
    }

    print("\nAll information is valid!")
    print("Campaign information saved:")
    print(campaign)

else:
    print("\nInvalid information. Nothing was saved.")

    if not name_valid:
        print("Campaign name must contain 3-30 letters, numbers or spaces.")

    if not email_valid:
        print("Please enter a valid email in the accepted format.")

    if not budget_valid:
        print("Budget must be a positive whole number.")
        


#checked all this 
# Campaign name:
# PASS: Flow Activewear
# FAIL: AB
# FAIL: Flow@Campaign
#
# Brand email:
# PASS: brand@example.com
# FAIL: brandexample.com
# FAIL: brand@com
#
# Campaign budget:
# PASS: 5000
# FAIL: 0
# FAIL: abc
#
# No surprising results expected with these rules.

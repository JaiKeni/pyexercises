"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# ANSWERS:
# 1. What goes in?
# Two sets of permissions represented as binary numbers.

# 2. What happens to it?
# Python combines permissions using bitwise OR,
# checks permissions using bitwise AND,
# adds permissions and removes permissions.

# 3. What comes out?
# The permissions at each step, displayed in binary.

# 4. What are your permissions about?
# My permissions are about managing a social media campaign.
# View campaign = 001
# Edit campaign = 010
# Publish campaign = 100


# INPUT: Define permissions
VIEW = 0b001
EDIT = 0b010
PUBLISH = 0b100

# Two users' permissions
designer_permissions = VIEW | EDIT
manager_permissions = VIEW | PUBLISH

print("SOCIAL MEDIA CAMPAIGN PERMISSIONS")
print("-" * 45)

# STEP 1: Display original permissions
print("Designer permissions:", format(designer_permissions, '03b'))
print("Manager permissions: ", format(manager_permissions, '03b'))

# STEP 2: Combine both permission sets
combined = designer_permissions | manager_permissions
print("\nCombined permissions:", format(combined, '03b'))

# STEP 3: Check if PUBLISH permission is present
has_publish = (combined & PUBLISH) != 0
print("Has publish permission:", has_publish)

# STEP 4: Add PUBLISH permission to the designer
designer_permissions = designer_permissions | PUBLISH
print("\nAfter adding PUBLISH:", format(designer_permissions, '03b'))

# STEP 5: Remove EDIT permission from the designer
designer_permissions = designer_permissions & ~EDIT
print("After removing EDIT: ", format(designer_permissions, '03b'))

print("-" * 45)

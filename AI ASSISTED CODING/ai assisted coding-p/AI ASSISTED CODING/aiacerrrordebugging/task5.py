# Prompt
# Fix this Python function:
# from typing import Type


def add_five(value):
    return value + 5

print(add_five("10"))

# Solution 1: Type Casting

def add_five(value):
    return int(value) + 5

print(add_five("10"))
# Output
# 15
# 3 Assert Test Cases
assert add_five("10") == 15
assert add_five("5") == 10
assert add_five("20") == 25

print("All test cases passed.")
# Output
# All test cases passed.
# Explanation

# "10" is a string, while 5 is an integer. Using int(value) converts the string "10" into the integer 10.

# Solution 2: String Concatenation

# If the purpose is to combine text rather than perform mathematical addition:

def add_five(value):
    return str(value) + "5"


print(add_five("10"))
# Output
# 105
# Difference
# Type Casting:
# "10" + 5 → 15

# String Concatenation:
# "10" + "5" → "105"
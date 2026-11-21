# Prompt
# Find and fix the error in this Python function:
def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"
# 3 Assert Test Cases
assert check_number(10) == "Ten"
assert check_number(5) == "Not Ten"
assert check_number(20) == "Not Ten"

print("All test cases passed.")
# Output
# All test cases passed.
# Explanation
# = is used for assignment.
# == is used for comparison.
# Therefore, n == 10 correctly checks whether n is equal to 10.
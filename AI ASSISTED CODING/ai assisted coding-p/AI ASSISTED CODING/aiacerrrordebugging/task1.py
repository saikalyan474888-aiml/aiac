# Prompt
# Find and fix the syntax error in this Python program:
# def greet():
#     print "Hello, AI Debugging Lab!"
# greet()
# Buggy Code
def greet():
    print ("Hello, AI Debugging Lab!")

greet()
# Error
# SyntaxError: Missing parentheses in call to 'print'
# Corrected Code
def greet():
    print("Hello, AI Debugging Lab!")

greet()
# 3 Assert Test Cases
def greet():
    return "Hello, AI Debugging Lab!"

assert greet() == "Hello, AI Debugging Lab!"
assert isinstance(greet(), str)
assert len(greet()) > 0
print(greet())
print("All test cases passed.")
# Output
# Hello, AI Debugging Lab!
# All test cases passed.
# Explanation

# In Python 3, print() is a function, so the message must be written inside parentheses.
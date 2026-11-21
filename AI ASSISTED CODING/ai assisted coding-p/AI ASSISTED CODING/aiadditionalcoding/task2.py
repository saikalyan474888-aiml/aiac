#PART A
#Gemini Prompt
#Write a simple Python program to check whether a given number is
#an Armstrong number. Explain the logic using comments and show
#sample input and output.
#Gemini Code
def is_armstrong(number):
    # Convert the number to a string to count its digits
    digits = str(number)
    power = len(digits)

    # Calculate the sum of each digit raised to the power
    total = sum(int(digit) ** power for digit in digits)

    # Check whether the sum is equal to the original number
    return total == number


number = 153

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
#output
# 153 is an Armstrong number
#PART B
#GitHub Copilot Prompt
# Create a Python function to check whether a number is an Armstrong
# number and print the result.
#copilot code
def is_armstrong(number):
    original = number
    digits = len(str(number))
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** digits
        number //= 10

    return total == original


number = 153

if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
#output
# 153 is an Armstrong number
#comparison
#Feature	                        Gemini	                             GitHub Copilot
# Code style	               Simple and compact     	                More traditional
# Digit extraction	    Converts number to string	              Uses mathematical operations
# Comments	                   Detailed	                             Fewer comments
# Readability                 	Very easy	                             Easy
# Logic	               Uses sum() and comprehension             	Uses while loop
# Beginner-friendly	             High	                                 High
# Code length	                   Shorter	                                 Longer
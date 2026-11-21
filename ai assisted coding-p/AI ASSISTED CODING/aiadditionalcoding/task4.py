#Part A – Original Code
#Code Written by Student
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_sum = 0
odd_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
#output
# Sum of even numbers: 30
# Sum of odd numbers: 25

#Part B - AI Refactoirng
#AI Prompt
# Refactor this Python program to make it shorter, more readable,
# and maintainable without changing its output. Use clear variable
# names and appropriate Python features.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_sum = 0
odd_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
#Refactored Code
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_sum = sum(number for number in numbers if number % 2 == 0)
odd_sum = sum(number for number in numbers if number % 2 != 0)

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
#output
# Sum of even numbers: 30
# Sum of odd numbers: 25
#improvements made
# Original Code	                      Refactored Code
# Uses a for loop	              Uses sum() with generator expressions
# More lines	                           Fewer lines
# Manual addition	                     Built-in sum()
# More repetitive	                      More concise
# Correct but longer	            Correct and maintainable
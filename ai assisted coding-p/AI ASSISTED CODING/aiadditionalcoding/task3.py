#Version 1 – Simple Prompt
#Cursor AI Prompt 1
#Write a simple Python program that checks whether a given year is
#a leap year.
#generated code
year = 2024

if year % 400 == 0:
    print(year, "is a leap year")
elif year % 100 == 0:
    print(year, "is not a leap year")
elif year % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
#output
# 2024 is a leap year

#Version 2 – Detailed Prompt
#Cursor AI Prompt 2
# Create a reusable Python function to check whether a year is a leap
# year. Take the year as user input, include comments, and handle
# the leap year rules correctly.
#generated code
def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 400, OR
    # 2. It is divisible by 4 but not divisible by 100

    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
#sample output
# Enter a year: 2024
#output
# 2024 is a leap year

#comparison
# Feature	                  Prompt 1        	      Prompt 2
# User input	                No	                   Yes
# Function	                No	                   Yes
# Comments	               Few	                 Detailed
# Reusability	               Low	                   High
# Code quality	          Basic	                  Better
# Suitable for application Less suitable      	More suitable
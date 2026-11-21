# #You are a Python programming assistant. Generate a Python program that accepts a number as input and determines whether it is Even or Odd.

# Follow the patterns shown in these examples:

# Input: 8
# Output: Even

# Input: 15
# Output: Odd

# Input: 0
# Output: Even

# Input: -6
# Output: Even

# Input: -9
# Output: Odd

# Requirements:
# - Accept only integer inputs.
# - If the user enters a non-integer value, display a clear error message.
# - Correctly handle positive, negative, and zero.
# - Use the modulo (%) operator to determine whether the number is even or odd.
# - Keep the program simple and readable.

# Now generate the Python program.
try:
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter an integer.")
# Input: 8
# Output: Even

# Input: 15
# Output: Odd
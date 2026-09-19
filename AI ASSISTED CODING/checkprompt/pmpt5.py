# You are a Python programming assistant.

# Generate a Python function named `is_perfect()` that accepts an integer and checks whether the number is a perfect number.

# Requirements:
# - A perfect number is a positive integer equal to the sum of its proper positive divisors, excluding the number itself.
# - Return `True` if the number is perfect; otherwise, return `False`.
# - Handle invalid values such as 0 and negative numbers appropriately.
# - Write clear and readable Python code.
# - Do not use external libraries.
# - Include a short explanation of the logic.

# Generate only the Python function and its explanation.
def is_perfect(n):
    if n <= 1:
        return False

    divisors_sum = 1  # Start with 1 since it's always a proper divisor for numbers > 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                divisors_sum += n // i
        i += 1

    return divisors_sum == n
n=int(input("Enter a positive integer to check if it's a perfect number: "))
try:
    print(f"The number {n} is a perfect number: {is_perfect(n)}")
except ValueError as e:
    print(e)    
print(is_perfect(n))      
# Input: 6
# Output: The number 6 is a perfect number: True
# True

# Input: 10
# Output: The number 10 is a perfect number: False
# False
#You are a Python programming assistant. Generate a Python function named `factorial()` that accepts a non-negative integer and returns its factorial.

def factorial(n):
    """
    Compute the factorial of a given number.
    
    Args:
        n: A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result
n=int(input("Enter a non-negative integer to compute its factorial: "))
try:
    print(f"The factorial of {n} is: {factorial(n)}")
except ValueError as e:
    print(e)
print(factorial(n))  # Example usage
# Input: 5
# Output: The factorial of 5 is: 120
# 120

# Input: 0
# Output: The factorial of 0 is: 1
# 1
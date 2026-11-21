#Generate a Python function named `is_armstrong()` that accepts a positive integer and returns `True` if the number is an Armstrong number, otherwise returns `False`.

def is_armstrong(n):
    """
    Check if a number is an Armstrong number.
    
    Args:
        n: A positive integer
        
    Returns:
        bool: True if the number is an Armstrong number, False otherwise
    """
    if n <= 0:
        return False
    
    # Convert the number to a string to easily access each digit
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the total equals the original number
    return total == n

# Example usage:
n = int(input("Enter a positive integer to check if it's an Armstrong number: "))
print(is_armstrong(n))
# Input: 153
# Output: True

# Input: 123
# Output: False
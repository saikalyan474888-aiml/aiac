#Generate a Python function that accepts a given number as input and determines whether the number is a palindrome. The function should return a clear Boolean result (`True` or `False`). Use clean, readable Python code and handle the input appropriately.
#Here is a Python function that checks if a given number is a palindrome:```python
def is_palindrome(num):
    """
    Check if a number is a palindrome.
    
    Args:
        num: An integer to check
        
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    if num < 0:
        return False
    
    str_num = str(num)
    return str_num == str_num[::-1]

num = int(input("Enter a number to check if it's a palindrome: "))
print(is_palindrome(num)) 
# Input: 121
# Output: True

# Input: 123
# Output: False
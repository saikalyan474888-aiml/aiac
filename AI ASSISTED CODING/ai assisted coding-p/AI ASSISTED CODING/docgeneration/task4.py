"""Functions for converting numbers between decimal, binary, and hexadecimal."""


def decimal_to_binary(n):
    """Convert a non-negative decimal integer to a binary string.

    Args:
        n (int): The non-negative decimal integer to convert.

    Returns:
        str: The binary representation of n without a ``0b`` prefix.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

    return bin(n)[2:]


def binary_to_decimal(b):
    """Convert a binary string to a decimal integer.

    Args:
        b (str): A non-empty string containing only 0 and 1 characters.

    Returns:
        int: The decimal value represented by b.

    Raises:
        TypeError: If b is not a string.
        ValueError: If b is empty or contains a character other than 0 or 1.
    """
    if not isinstance(b, str):
        raise TypeError("b must be a string.")
    if not b or any(character not in "01" for character in b):
        raise ValueError("b must contain only 0 and 1.")

    return int(b, 2)


def decimal_to_hexadecimal(n):
    """Convert a non-negative decimal integer to a hexadecimal string.

    Args:
        n (int): The non-negative decimal integer to convert.

    Returns:
        str: The uppercase hexadecimal representation of n without a ``0x`` prefix.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")

    return hex(n)[2:].upper()
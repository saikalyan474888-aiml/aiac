def is_strong_password(password):
    # A strong password must be at least 8 characters long.
    if len(password) < 8:
        return False

    # Spaces are not allowed.
    if " " in password:
        return False

    # Check for at least one uppercase letter.
    has_upper = any(char.isupper() for char in password)

    # Check for at least one lowercase letter.
    has_lower = any(char.islower() for char in password)

    # Check for at least one digit.
    has_digit = any(char.isdigit() for char in password)

    # Check for at least one special character.
    # A special character is anything that is not a letter or number.
    has_special = any(not char.isalnum() for char in password)

    # Return True only if all rules are satisfied.
    return has_upper and has_lower and has_digit and has_special


# Tests: write the checks after the function.
# These assertions describe what the function should do.
assert is_strong_password("Abcd@123") == True
assert is_strong_password("abcd123") == False
assert is_strong_password("ABCD@1234") == False

# Extra edge-case tests
assert is_strong_password("Abcdef1!") == True
assert is_strong_password("Abc d@123") == False


# This message prints only if all tests pass.
print("All Task 1 tests passed!")
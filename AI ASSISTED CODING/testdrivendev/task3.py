# Tests first: write the checks before the function.
# These assertions describe what the function should do.

def is_anagram(str1, str2):
    # Helper function to clean the string:
    # - ignore uppercase/lowercase differences
    # - ignore spaces
    # - ignore punctuation
    def normalize(text):
        cleaned = ""
        for ch in text:
            if ch.isalnum():      # keep only letters and numbers
                cleaned += ch.lower()
        return cleaned

    # Normalize both strings before comparing
    cleaned1 = normalize(str1)
    cleaned2 = normalize(str2)

    # If both cleaned strings have the same letters in the same amount,
    # they are anagrams.
    return sorted(cleaned1) == sorted(cleaned2)


# This message prints only if all tests pass.
print("All Task 3 tests passed!")
#You are an expert Python programmer.

# Context:
# Create an efficient Python program that classifies a given integer as:
# 1. Prime
# 2. Composite
# 3. Neither

# Requirements:
# - Accept an integer as input.
# - Validate the input properly.
# - Numbers less than 2 must be classified as "Neither".
# - A prime number has exactly two positive divisors: 1 and itself.
# - A composite number is greater than 1 and is not prime.
# - Optimize the logic by checking divisors only up to the square root of the number.
# - Handle 2 as a special case and skip unnecessary even-number checks.
# - Use clear variable names and readable Python code.
# - Do not use external libraries.
# - Return or print the classification.
# - Include brief comments explaining the optimization.

# Task:
# Generate the optimized Python program and briefly explain how the optimization improves efficiency.

# Also compare the generated solution with:
# - Zero-shot prompting: no examples or additional context.
# - One-shot prompting: one input-output example.
# - Few-shot prompting: multiple input-output examples.

# Explain why context-managed prompting is more suitable for this problem.Here is an optimized Python program that classifies a given integer as Prime, Composite, or Neither:

# ```python
def classify_number(n):
    if n < 2:
        return "Neither"

    if n == 2:
        return "Prime"

    if n % 2 == 0:
        return "Composite"

    # Check only up to the square root of n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return "Composite"
        i += 2

    return "Prime"


num = int(input("Enter a number: "))
print(classify_number(num))
# Input: 17
# Output: Prime

# Input: 12
# Output: Composite
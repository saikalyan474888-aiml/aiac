# Python Program
numbers = [10, 15, 20, 25, 30, 35]

# even_count = 0
# odd_count = 0
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1


# print("Even numbers:", even_count)
# print("Odd numbers:", odd_count)
# Output
# Even numbers: 3
# Odd numbers: 3
# Logic Flow
# Start
#   ↓
# Take each number from the list
#   ↓
# Check num % 2 == 0
#   ↓
# Yes → Increase even_count
# No  → Increase odd_count
#   ↓
# Repeat until list ends
#   ↓
# Display counts

# Lab 12 - Question 4: Bubble Sort
# Student Marks Sorting

# Student records: [Roll Number, Name, Marks]
students = [
    [101, "Ravi", 85],
    [102, "Priya", 65],
    [103, "Arjun", 90],
    [104, "Sneha", 70],
    [105, "Kiran", 80]
]

print("Original Student Records:")
for student in students:
    print(student)

# Apply Bubble Sort
n = len(students)

for i in range(n - 1):

    # Compare adjacent student marks
    for j in range(n - i - 1):

        # Swap if previous marks are greater
        if students[j][2] > students[j + 1][2]:
            students[j], students[j + 1] = students[j + 1], students[j]

    # Display records after each pass
    print("\nAfter pass", i + 1, ":")
    for student in students:
        print(student)

# Display final sorted records
print("\nSorted Student Records (Ascending Marks):")
for student in students:
    print(student)


# OUTPUT:
# Original Student Records:
# [101, 'Ravi', 85]
# [102, 'Priya', 65]
# [103, 'Arjun', 90]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
#
# After pass 1 :
# [102, 'Priya', 65]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
# [101, 'Ravi', 85]
# [103, 'Arjun', 90]
#
# After pass 2 :
# [102, 'Priya', 65]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
# [101, 'Ravi', 85]
# [103, 'Arjun', 90]
#
# After pass 3 :
# [102, 'Priya', 65]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
# [101, 'Ravi', 85]
# [103, 'Arjun', 90]
#
# After pass 4 :
# [102, 'Priya', 65]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
# [101, 'Ravi', 85]
# [103, 'Arjun', 90]
#
# Sorted Student Records (Ascending Marks):
# [102, 'Priya', 65]
# [104, 'Sneha', 70]
# [105, 'Kiran', 80]
# [101, 'Ravi', 85]
# [103, 'Arjun', 90]
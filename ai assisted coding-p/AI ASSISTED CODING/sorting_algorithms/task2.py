
# Lab 12 - Question 2: Merge Sort
# Hospital Patient Records

# Patient records: [Patient ID, Patient Name, Medical Bill]
patients = [
    [101, "Ravi", 5000],
    [102, "Priya", 3000],
    [103, "Arjun", 7000],
    [104, "Sneha", 2000],
    [105, "Kiran", 4000]
]

# Merge two sorted halves
def merge(left, right):
    result = []

    while left and right:
        if left[2] <= right[2]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left)
    result.extend(right)

    print("Merging:", [(p[0], p[2]) for p in result])
    return result


# Divide and conquer using Merge Sort
def merge_sort(records):

    if len(records) <= 1:
        return records

    mid = len(records) // 2

    left = records[:mid]
    right = records[mid:]

    print("Splitting:", [p[2] for p in records])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# Display original records
print("Original Patient Records:")
for p in patients:
    print(p)

# Sort records by medical bill
sorted_patients = merge_sort(patients)

# Display sorted records
print("\nSorted Patient Records (By Bill Amount):")
for p in sorted_patients:
    print(p)


# OUTPUT:
# Original Patient Records:
# [101, 'Ravi', 5000]
# [102, 'Priya', 3000]
# [103, 'Arjun', 7000]
# [104, 'Sneha', 2000]
# [105, 'Kiran', 4000]
#
# Splitting: [5000, 3000, 7000, 2000, 4000]
# Splitting: [5000, 3000]
# Splitting: [7000, 2000, 4000]
# Splitting: [2000, 4000]
# Merging: [(104, 2000), (105, 4000)]
# Merging: [(103, 7000), (104, 2000), (105, 4000)]
# Merging: [(102, 3000), (101, 5000)]
# Merging: [(102, 3000), (101, 5000), (103, 7000), (104, 2000), (105, 4000)]
#
# Sorted Patient Records (By Bill Amount):
# [104, 'Sneha', 2000]
# [102, 'Priya', 3000]
# [105, 'Kiran', 4000]
# [101, 'Ravi', 5000]
# [103, 'Arjun', 7000]
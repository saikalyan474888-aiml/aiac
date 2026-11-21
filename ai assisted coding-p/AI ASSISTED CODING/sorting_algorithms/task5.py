
# Lab 12 - Question 5: Quick Sort
# Examination Result Processing

# Student records: [Roll Number, Name, Total Marks]
students = [
    [101, "Ravi", 85],
    [102, "Priya", 65],
    [103, "Arjun", 90],
    [104, "Sneha", 70],
    [105, "Kiran", 80]
]

# Display original records
print("Original Student Records:")
for student in students:
    print(student)


# Partition function using last element as pivot
def partition(arr, low, high):

    # Select last element as pivot
    pivot = arr[high][2]

    # Index of smaller element
    i = low - 1

    # Compare elements with pivot
    for j in range(low, high):

        # Arrange greater marks before pivot
        if arr[j][2] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print("Pivot:", pivot, "Array:", [s[2] for s in arr])

    return i + 1


# Quick Sort function
def quick_sort(arr, low, high):

    if low < high:

        # Find partition index
        pi = partition(arr, low, high)

        # Sort left part
        quick_sort(arr, low, pi - 1)

        # Sort right part
        quick_sort(arr, pi + 1, high)


# Apply Quick Sort
quick_sort(students, 0, len(students) - 1)

# Display sorted records
print("\nSorted Student Records (Descending Marks):")
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
# Pivot: 80 Array: [85, 90, 80, 70, 65]
# Pivot: 65 Array: [85, 90, 80, 70, 65]
# Pivot: 70 Array: [85, 90, 80, 70, 65]
# Pivot: 85 Array: [90, 85, 80, 70, 65]
#
# Sorted Student Records (Descending Marks):
# [103, 'Arjun', 90]
# [101, 'Ravi', 85]
# [105, 'Kiran', 80]
# [104, 'Sneha', 70]
# [102, 'Priya', 65]
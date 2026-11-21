
# Q1. Bubble Sort
# Sort elements in ascending order

arr = [45, 12, 78, 34, 23, 56, 10]

print("Original Array:", arr)

n = len(arr)

# Apply Bubble Sort
for i in range(n - 1):

    # Compare adjacent elements
    for j in range(n - i - 1):

        # Swap if left element is greater
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # Display array after each pass
    print("After Pass", i + 1, ":", arr)

# Display sorted array
print("Sorted Array:", arr)


# OUTPUT:
# Original Array: [45, 12, 78, 34, 23, 56, 10]
# After Pass 1 : [12, 45, 34, 23, 56, 10, 78]
# After Pass 2 : [12, 34, 23, 45, 10, 56, 78]
# After Pass 3 : [12, 23, 34, 10, 45, 56, 78]
# After Pass 4 : [12, 23, 10, 34, 45, 56, 78]
# After Pass 5 : [12, 10, 23, 34, 45, 56, 78]
# After Pass 6 : [10, 12, 23, 34, 45, 56, 78]
# Sorted Array: [10, 12, 23, 34, 45, 56, 78]
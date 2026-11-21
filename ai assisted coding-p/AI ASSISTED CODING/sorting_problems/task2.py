
# Q2. Selection Sort
# Sort elements in ascending order

arr = [64, 25, 12, 22, 11, 90]

print("Original Array:", arr)

n = len(arr)

# Apply Selection Sort
for i in range(n):

    # Assume current element is minimum
    min_index = i

    # Find minimum element
    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Display minimum element selected
    print("Pass", i + 1, "- Minimum Element:", arr[min_index])

    # Swap minimum with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

    # Display array after each pass
    print("After Pass", i + 1, ":", arr)

# Display sorted array
print("Sorted Array:", arr)


# OUTPUT:
# Original Array: [64, 25, 12, 22, 11, 90]
# Pass 1 - Minimum Element: 11
# After Pass 1 : [11, 25, 12, 22, 64, 90]
# Pass 2 - Minimum Element: 12
# After Pass 2 : [11, 12, 25, 22, 64, 90]
# Pass 3 - Minimum Element: 22
# After Pass 3 : [11, 12, 22, 25, 64, 90]
# Pass 4 - Minimum Element: 25
# After Pass 4 : [11, 12, 22, 25, 64, 90]
# Pass 5 - Minimum Element: 64
# After Pass 5 : [11, 12, 22, 25, 64, 90]
# Pass 6 - Minimum Element: 90
# After Pass 6 : [11, 12, 22, 25, 64, 90]
# Sorted Array: [11, 12, 22, 25, 64, 90]
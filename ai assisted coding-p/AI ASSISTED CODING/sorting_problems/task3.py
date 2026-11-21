
# Q3. Insertion Sort
# Sort elements in ascending order

arr = [40, 20, 10, 50, 30, 60]

print("Original Array:", arr)

# Apply Insertion Sort
for i in range(1, len(arr)):

    # Select key element
    key = arr[i]

    # Start comparing with previous element
    j = i - 1

    print("\nPass", i, "- Key Element:", key)

    # Compare and shift elements
    while j >= 0 and arr[j] > key:

        print("Comparison:", arr[j], ">", key, "- Shift")

        # Shift element to the right
        arr[j + 1] = arr[j]

        j -= 1

    # Insert key into correct position
    arr[j + 1] = key

    print("Insert Key:", key)
    print("After Pass", i, ":", arr)

# Display sorted array
print("\nSorted Array:", arr)


# OUTPUT:
# Original Array: [40, 20, 10, 50, 30, 60]
#
# Pass 1 - Key Element: 20
# Comparison: 40 > 20 - Shift
# Insert Key: 20
# After Pass 1 : [20, 40, 10, 50, 30, 60]
#
# Pass 2 - Key Element: 10
# Comparison: 40 > 10 - Shift
# Comparison: 20 > 10 - Shift
# Insert Key: 10
# After Pass 2 : [10, 20, 40, 50, 30, 60]
#
# Pass 3 - Key Element: 50
# Insert Key: 50
# After Pass 3 : [10, 20, 40, 50, 30, 60]
#
# Pass 4 - Key Element: 30
# Comparison: 50 > 30 - Shift
# Comparison: 40 > 30 - Shift
# Insert Key: 30
# After Pass 4 : [10, 20, 30, 40, 50, 60]
#
# Pass 5 - Key Element: 60
# Insert Key: 60
# After Pass 5 : [10, 20, 30, 40, 50, 60]
#
# Sorted Array: [10, 20, 30, 40, 50, 60]
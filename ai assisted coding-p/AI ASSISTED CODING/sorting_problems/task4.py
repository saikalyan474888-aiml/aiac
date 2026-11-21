
# Q4. Merge Sort
# Divide and Conquer Algorithm

arr = [38, 27, 43, 3, 9, 82, 10, 15]

print("Original Array:", arr)

# Merge two sorted subarrays
def merge(left, right):

    result = []

    while left and right:

        # Compare elements and select smaller
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Add remaining elements
    result.extend(left)
    result.extend(right)

    print("Merging:", result)

    return result


# Divide array recursively
def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Find middle position
    mid = len(arr) // 2

    # Divide into two halves
    left = arr[:mid]
    right = arr[mid:]

    print("Splitting:", arr)

    # Recursive calls
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    return merge(left, right)


# Apply Merge Sort
sorted_arr = merge_sort(arr)

# Display sorted array
print("\nSorted Array:", sorted_arr)


# OUTPUT:
# Original Array: [38, 27, 43, 3, 9, 82, 10, 15]
# Splitting: [38, 27, 43, 3, 9, 82, 10, 15]
# Splitting: [38, 27, 43, 3]
# Splitting: [38, 27]
# Splitting: [43, 3]
# Splitting: [9, 82, 10, 15]
# Splitting: [9, 82]
# Splitting: [10, 15]
# Merging: [27, 38]
# Merging: [3, 43]
# Merging: [3, 27, 38, 43]
# Merging: [9, 82]
# Merging: [10, 15]
# Merging: [9, 10, 15, 82]
# Merging: [3, 9, 10, 15, 27, 38, 43, 82]
#
# Sorted Array: [3, 9, 10, 15, 27, 38, 43, 82]
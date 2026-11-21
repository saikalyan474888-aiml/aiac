
# Q5. Quick Sort
# Last element is selected as pivot

arr = [50, 30, 70, 10, 90, 20, 60]

print("Original Array:", arr)


# Partition function
def partition(arr, low, high):

    # Select last element as pivot
    pivot = arr[high]

    # Initialize smaller element index
    i = low - 1

    # Compare elements with pivot
    for j in range(low, high):

        if arr[j] < pivot:

            # Increment index
            i += 1

            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    print("Pivot:", pivot, "Array:", arr)

    return i + 1


# Quick Sort function
def quick_sort(arr, low, high):

    if low < high:

        # Find partition position
        pi = partition(arr, low, high)

        # Recursive call for left subarray
        quick_sort(arr, low, pi - 1)

        # Recursive call for right subarray
        quick_sort(arr, pi + 1, high)


# Apply Quick Sort
quick_sort(arr, 0, len(arr) - 1)

# Display sorted array
print("\nSorted Array:", arr)


# OUTPUT:
# Original Array: [50, 30, 70, 10, 90, 20, 60]
# Pivot: 60 Array: [50, 30, 10, 20, 60, 90, 70]
# Pivot: 20 Array: [10, 20, 50, 30, 60, 90, 70]
# Pivot: 30 Array: [10, 20, 30, 50, 60, 90, 70]
# Pivot: 70 Array: [10, 20, 30, 50, 60, 70, 90]
#
# Sorted Array: [10, 20, 30, 50, 60, 70, 90]
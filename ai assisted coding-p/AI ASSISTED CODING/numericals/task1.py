
# Q1. Binary Search
# Search for key 30

arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
key = 30

low = 0
high = len(arr) - 1
count = 0

print("Array:", arr)

# Apply Binary Search
while low <= high:

    mid = (low + high) // 2
    count += 1

    print("Low:", low, "High:", high, "Mid:", mid)
    print("Middle Element:", arr[mid])

    if arr[mid] == key:
        print("Element Found at Index:", mid)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

print("Total Comparisons:", count)


# OUTPUT:
# Array: [5, 10, 15, 20, 25, 30, 35, 40, 45]
# Low: 0 High: 8 Mid: 4
# Middle Element: 25
# Low: 5 High: 8 Mid: 6
# Middle Element: 35
# Low: 5 High: 5 Mid: 5
# Middle Element: 30
# Element Found at Index: 5
# Total Comparisons: 3
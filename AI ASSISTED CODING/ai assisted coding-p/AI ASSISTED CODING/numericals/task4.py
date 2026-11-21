
# Q4. Binary Search
# Search for key 47

arr = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]
key = 47

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
# Array: [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]
# Low: 0 High: 14 Mid: 7
# Middle Element: 31
# Low: 8 High: 14 Mid: 11
# Middle Element: 47
# Element Found at Index: 11
# Total Comparisons: 2
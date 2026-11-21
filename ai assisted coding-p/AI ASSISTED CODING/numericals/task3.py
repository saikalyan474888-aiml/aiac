
# Q3. Binary Search
# Search for first element 8

arr = [8, 16, 24, 32, 40, 48, 56, 64, 72]
key = 8

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
# Array: [8, 16, 24, 32, 40, 48, 56, 64, 72]
# Low: 0 High: 8 Mid: 4
# Middle Element: 40
# Low: 0 High: 3 Mid: 1
# Middle Element: 16
# Low: 0 High: 0 Mid: 0
# Middle Element: 8
# Element Found at Index: 0
# Total Comparisons: 3
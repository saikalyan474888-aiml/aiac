
# Q2. Binary Search
# Search for key 50 (Not Present)

arr = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
key = 50

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

else:
    print("Element Not Found")

print("Total Comparisons:", count)


# OUTPUT:
# Array: [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
# Low: 0 High: 9 Mid: 4
# Middle Element: 36
# Low: 5 High: 9 Mid: 7
# Middle Element: 54
# Low: 5 High: 6 Mid: 5
# Middle Element: 42
# Low: 6 High: 6 Mid: 6
# Middle Element: 48
# Element Not Found
# Total Comparisons: 4
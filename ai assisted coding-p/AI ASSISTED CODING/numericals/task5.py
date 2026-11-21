
# Q5. Modified Binary Search
# Find the first occurrence of key 20

arr = [10, 20, 20, 20, 30, 40, 50, 60, 70]
key = 20

low = 0
high = len(arr) - 1

result = -1
count = 0

print("Array:", arr)

# Apply Modified Binary Search
while low <= high:

    mid = (low + high) // 2
    count += 1

    print("Low:", low, "High:", high, "Mid:", mid)
    print("Middle Element:", arr[mid])

    if arr[mid] == key:

        # Store the found index
        result = mid

        # Continue searching on the left side
        high = mid - 1

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

# Display first occurrence
if result != -1:
    print("First Occurrence Found at Index:", result)
else:
    print("Element Not Found")

print("Total Iterations:", count)


# OUTPUT:
# Array: [10, 20, 20, 20, 30, 40, 50, 60, 70]
# Low: 0 High: 8 Mid: 4
# Middle Element: 30
# Low: 0 High: 3 Mid: 1
# Middle Element: 20
# Low: 0 High: 0 Mid: 0
# Middle Element: 10
# First Occurrence Found at Index: 1
# Total Iterations: 3
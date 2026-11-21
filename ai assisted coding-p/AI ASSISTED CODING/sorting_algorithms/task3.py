
# Lab 12 - Question 3: Selection Sort
# Product Price Management

# Store product prices
prices = [450, 200, 600, 150, 350]

print("Original Prices:", prices)

# Apply Selection Sort
for i in range(len(prices)):

    # Assume current element is minimum
    min_index = i

    # Find minimum element in remaining array
    for j in range(i + 1, len(prices)):
        if prices[j] < prices[min_index]:
            min_index = j

    # Swap minimum element with current element
    prices[i], prices[min_index] = prices[min_index], prices[i]

    # Display array after each pass
    print("After pass", i + 1, ":", prices)

# Display sorted prices
print("Sorted Prices:", prices)


# OUTPUT:
# Original Prices: [450, 200, 600, 150, 350]
# After pass 1 : [150, 200, 600, 450, 350]
# After pass 2 : [150, 200, 600, 450, 350]
# After pass 3 : [150, 200, 350, 450, 600]
# After pass 4 : [150, 200, 350, 450, 600]
# After pass 5 : [150, 200, 350, 450, 600]
# Sorted Prices: [150, 200, 350, 450, 600]
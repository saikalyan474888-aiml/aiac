#Generate a code which takes sample_list a variable that takes input of numbers and a function named product_odd(sample_list) which checks whether the numbers are odd and gives product of odd numbers in the list.    1
def product_odd(sample_list):
    product = 1
    found = False

    for num in sample_list:
        if num % 2 != 0:
            product *= num
            found = True

    if found:
        return product
    else:
        return 0


sample_list = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = product_odd(sample_list)
print("Product of odd numbers:", result)
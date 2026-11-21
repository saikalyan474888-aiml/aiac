
# Insertion Sort - Employee Salary Management

salary = [50000, 30000, 70000, 20000, 40000]

print("Original Salaries:", salary)

for i in range(1, len(salary)):
    key = salary[i]
    j = i - 1

    while j >= 0 and salary[j] > key:
        salary[j + 1] = salary[j]
        j = j - 1

    salary[j + 1] = key

    print("After iteration", i, ":", salary)

print("Sorted Salaries:", salary)

#output:
# Original Salaries: [50000, 30000, 70000, 20000, 40000]

# After iteration 1 : [30000, 50000, 70000, 20000, 40000]
# After iteration 2 : [30000, 50000, 70000, 20000, 40000]
# After iteration 3 : [20000, 30000, 50000, 70000, 40000]
# After iteration 4 : [20000, 30000, 40000, 50000, 70000]

# Sorted Salaries: [20000, 30000, 40000, 50000, 70000]
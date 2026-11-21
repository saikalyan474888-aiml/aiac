#Task 1: Print Even Numbers from 1 to N

#Prompt:
#“Generate Python code to print all even numbers between 1 and N using a loop.”

#Python Program
n = int(input("Enter N: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

#Loop Used
#for loop

# Sample Input and Output
# Input: 10
# Output:
# 2
# 4
# 6
# 8
# 10
# Logic

# The loop checks every number from 1 to N. If i % 2 == 0, the number is even, so it is printed.
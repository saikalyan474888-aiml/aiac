class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)


student = Student("saikalyan", 101, [80, 75, 90])

print("Name:", student.name)
print("Roll Number:", student.roll_number)
print("Total Marks:", student.calculate_total())
print("Average Marks:", student.calculate_average())

# Output
# Name: saikalyan
# Roll Number: 101
# Total Marks: 245
# Average Marks: 81.66666666666667
# Minor Improvement

# To make the average easier to read:

print("Average Marks:", round(student.calculate_average(), 2))

# Output:

# Average Marks: 81.67

# Justification: Rounding the average to two decimal places improves readability without changing the calculation.
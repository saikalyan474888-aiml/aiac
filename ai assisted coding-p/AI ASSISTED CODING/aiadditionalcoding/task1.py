#Prompt Given to Gemini
#Write a Python function that accepts a list of numbers and calculates
#the mean, minimum, and maximum values. Include comments and display
#the results for a sample list.
#Gemini-Generated Code
def calculate_statistics(numbers):
    # Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)

    # Find the minimum value
    minimum = min(numbers)

    # Find the maximum value
    maximum = max(numbers)

    return mean, minimum, maximum


# Sample survey data
survey_data = [10, 20, 30, 40, 50]

mean, minimum, maximum = calculate_statistics(survey_data)

print("Mean:", mean)
print("Minimum:", minimum)
print("Maximum:", maximum)
#output
# Mean: 30.0
# Minimum: 10
# Maximum: 50
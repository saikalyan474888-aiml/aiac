def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(50))
# Output
# A
# B
# C
# D
# F
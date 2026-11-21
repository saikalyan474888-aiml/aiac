class User:
    def __init__(self, age, email):
        self.age = age
        self.email = email

    def validate(self):
        if self.age >= 18:
            age_valid = True
        else:
            age_valid = False

        if "@" in self.email and "." in self.email:
            email_valid = True
        else:
            email_valid = False

        return age_valid, email_valid

user = User(20, "student@example.com")

age_valid, email_valid = user.validate()

print("Age valid:", age_valid)
print("Email valid:", email_valid)

# Output
# Age valid: True
# Email valid: True

# Invalid Test Case
user = User(16, "studentexample.com")
age_valid, email_valid = user.validate()
print("Age valid:", age_valid)
print("Email valid:", email_valid)

# Output
# Age valid: False
# Email valid: False
# Logic
# Age 18 or above → valid.
# Age below 18 → invalid.
# Email containing @ and . → valid.
# Otherwise → invalid.
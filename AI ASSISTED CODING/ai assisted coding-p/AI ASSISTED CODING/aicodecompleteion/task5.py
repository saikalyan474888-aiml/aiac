class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Keerthana", 5000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
#  Sample Output
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 1
# Enter deposit amount: 2000
# Amount deposited successfully.

# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 3
# Current Balance: 7000.0

# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 2
# Enter withdrawal amount: 1000
# Amount withdrawn successfully.

# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice: 3
# Current Balance: 6000.0
# Strengths of AI Suggestions
# Generates code quickly.
# Helps create classes and functions.
# Reduces coding time.
# Provides a basic structure that can be manually improved.
# Limitations
# AI-generated code may contain logical errors.
# The programmer must test the code.
# AI may not always handle all edge cases.
# The generated code should be understood before using it.
# Reflection

# AI-assisted coding improves productivity by providing code suggestions quickly and helping programmers create a basic solution. However, the programmer must verify, test, and understand the generated code before using it.
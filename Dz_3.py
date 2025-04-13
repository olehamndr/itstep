class BankAccount:
    def __init__(self, account_number=0, balance=0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount=0):
        if amount > 0:
            self.balance = self.balance + amount
            print(amount, "UAH has been deposited. Current balance:", self.balance, "UAH.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount=0):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds in the account.")
        else:
            self.balance = self.balance - amount
            print(amount, "UAH has been withdrawn. Current balance:", self.balance, "UAH.")

    def show_balance(self):
        print("Account number:", self.account_number,", Balance:", self.balance, "UAH")

account = BankAccount(str(input("Enter your acuunt number: ")))

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Show balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
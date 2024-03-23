class BankAccount:
    def __init__(self, account_holder_name, account_number, balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance
        print("Bank Account Created. Your current balance is 0$")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, you don't have enough money to withdraw")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Now your balance is: {self.balance}$")


name = input("Enter your name to create an account: ")
my_account = BankAccount(name, '123456789')
my_account.deposit(float(input("Enter the number of deposit you want to add: ")))
my_account.display_balance()
my_account.withdraw(float(input("Enter the number of withdrawal: ")))
my_account.display_balance()

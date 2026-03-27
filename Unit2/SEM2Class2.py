class BankAccount:
    def __init__(self, account_num, balance=0.0):
        self.account = account_num
        self.balance = balance

    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient balance.")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"Deposit of ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("The deposit amount must be positive")

    def CheckBalance(self):
        print(f'The balance of account number {self.account} is {self.balance}')

Account1 = BankAccount("HDFC1000", 100000)
Account1.withdraw(1100)
Account1.deposit(1100)
Account1.CheckBalance()



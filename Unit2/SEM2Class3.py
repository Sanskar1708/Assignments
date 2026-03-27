# Base wala class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

#Creating objects
car = Car()
bike = Bicycle()

car.move()   
bike.move()  


class BankAccount:
    def __init__(self, account_num, balance=0.0):
        self.account = account_num
        self.balance = balance

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("The deposit amount must be positive.")

    def check_balance(self):
        print(f'The balance of account number {self.account} is ₹{self.balance:.2f}')

while True:
    # Get account details
    account_num = input("Enter account number: ")
    try:
        initial_balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance. Using 0.0")
        initial_balance = 0.0
    
    account = BankAccount(account_num, initial_balance)
    
    # Main menu loop
    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Select option (1-4): ")
        
        if choice == '1':
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
                
        elif choice == '2':
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
                
        elif choice == '3':
            account.check_balance()
            
        elif choice == '4':
            print("Thank you for banking with us!")
            break  # Exit inner loop, restart outer loop
            
        else:
            print("Invalid option. Please select 1-4.")
import random

class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0  
        self.total_loan_amount = 0  
        self.loan_feature = True 

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100, 999)
        account = Account(name, email, address, account_type, account_number)
        self.accounts.append(account)
        print(f"Account created user {name}. Account Number: {account_number}")
        # return account_number

    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"{account_number} is deleted !")
                return
            
        print(f"{account_number} is not found !")

    def show_users(self):
        if not self.accounts:
            print("No users !")
        else:
            for account in self.accounts:
                print(f"Name: {account.name}, Account Number: {account.account_number}, Account Type: {account.account_type}")
    
    def show_total_balance(self):
        total = sum(account.balance for account in self.accounts)
        print(f"Total Balance: {total}")

    def show_total_loan(self):
        print(f"Total Loan: {self.total_loan_amount}")

    def on_loan(self):
        self.loan_feature = True
        print("Loan feature has been turned ON.")

    def off_loan(self):
        self.loan_feature = False
        print("Loan feature has been turned OFF.")

    

class Account:
    def __init__(self, name, email, address, account_type, account_number):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_number = account_number
        self.balance = 0
        self.transactions = []
        self.loan_count = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"{amount} is deposited to account {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal amount exceeded.")
        else:    
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Withdrawn {amount} from account {self.account_number}")

    def show_balance(self):
        print(f"Balance: {self.balance}")

    def show_transactions(self):
        if not self.transactions:
            print("No transaction !")
        else:
            for transaction in self.transactions:
                print(transaction)

    def take_loan(self, amount, bank):
        if not bank.loan_feature:
            print("Loan feature is currently OFF.")
        elif self.loan_count >= 2:
            print("Sorry, loan limit reached. Only 2 loans are allowed.")
        else:
            self.balance += amount
            self.loan_count += 1
            bank.total_loan_amount += amount
            self.transactions.append(f"Loan of {amount} taken")
            print(f"Loan of {amount} approved for account {self.account_number}.")

    def make_transfer(self, receiver_account, amount, bank):
        if receiver_account not in [account.account_number for account in bank.accounts]:
            print("Account does not exist.")
        elif amount > self.balance:
            print("Not enough balance.")
        else:
            for account in bank.accounts:
                if account.account_number == receiver_account:
                    account.balance += amount
                    self.balance -= amount
                    self.transactions.append(f"Transferred {amount} to {receiver_account}")
                    print(f"Transferred {amount} to account {receiver_account}")
                    return

def main():
    bank = Bank()

    while True:
        print("\n===== Banking System =====")
        print("1. Admin Login")
        print("2. User Login")
        print("3. User Create Account")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            admin_menu(bank)
        elif choice == "2":
            user_login(bank)
        elif choice == "3":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
            user_login(bank)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

def admin_menu(bank):
    while True:
        print("\n===== Admin Menu =====")
        print("1. Create Account")
        print("2. Delete User Account")
        print("3. Show All Users")
        print("4. Check Total Balance")
        print("5. Show Total Loan")
        print("6. Turn OFF Loan Feature")
        print("7. Turn ON Loan Feature")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            bank.create_account(name, email, address, account_type)
        elif choice == "2":
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == "3":
            bank.show_users()
        elif choice == "4":
            bank.show_total_balance()
        elif choice == "5":
            bank.show_total_loan()
        elif choice == "6":
            bank.off_loan()
        elif choice == "7":
            bank.on_loan()
        elif choice == "8":
            break
        else:
            print("Invalid choice!")

def user_login(bank):
    account_number = int(input("Enter your account number: "))
    
    for account in bank.accounts:
        if account.account_number == account_number:
            user_menu(account, bank)
            return
    
    print("No Account!")

def user_menu(account, bank):
    while True:
        print("\n===== User Menu =====")
        print(f"Logged in as {account.name}")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Show Transaction History")
        print("5. Transfer Money")
        print("6. Request Loan")
        print("7. Exit User Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_transactions()
        elif choice == "5":
            recipient_account = int(input("Enter recipient account number: "))
            amount = float(input("Enter amount to transfer: "))
            account.make_transfer(recipient_account, amount, bank)
        elif choice == "6":
            amount = float(input("Enter loan amount: "))
            account.take_loan(amount, bank)
        elif choice == "7":
            break
        else:
            print("Invalid choice!")
main()
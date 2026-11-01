class BankAccount:
    # Constructor to initialize attributes
    def __init__(self, acc_number, holder_name, acc_type, balance=0.0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.acc_type = acc_type
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount!")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew: ${amount:.2f}")
        else:
            print("Insufficient balance or invalid amount!")

    # Method to display account details and current balance
    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.acc_number}")
        print(f"Holder Name    : {self.holder_name}")
        print(f"Account Type   : {self.acc_type}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-----------------------\n")

def main():
    acc = BankAccount(
        input("A/C No: "),
        input("Name: "),
        input("Type: "),
        float(input("Balance: "))
    )
    
    while True:
        ch = input("1.Deposit 2.Withdraw 3.Display 4.Exit: ")
        if ch == "1": acc.deposit(float(input("Amount: ")))
        elif ch == "2": acc.withdraw(float(input("Amount: ")))
        elif ch == "3": acc.display_details()  # Fixed name here
        elif ch == "4": break

if __name__ == "__main__":
    main()
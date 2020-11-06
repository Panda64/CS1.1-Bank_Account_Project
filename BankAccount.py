import random

def random_bank_account_number():
    num = random.randrange(1, 10000**2)
    num_with_zeros = '{:08}'.format(num)
    
    return num_with_zeros

class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name

    account_number = random_bank_account_number()
    routing_number = 123456789
    balance = 0

    def deposit(self, amount):
        balance += amount

        print(f"Amount Deposited: ${amount}")

    def withdrawl(self, amount):
        if amount > balance:
            print("Insufficient funds. You will be charged a $10 overdraft fee if you withdraw this amount. \
                   Do you wish to continue? (y/n) ")
            
            retry = True

            while retry:
                user_input = input()

                if user_input == 'y' or user_input == 'Y':
                    balance -= (amount + 10)
                    print(f"Withdraw confirmed, you will be charged a $10 overdraft fee. Amount Withdrawn: ${amount}")
                    retry = False
                elif user_input == 'n' or user_input == 'N':
                    "Withdraw canceled."
                    retry = False
                else:
                    print("Please type either 'y' or 'n'. Try again.")
        else:
            balance -= amount

    def get_balance(self):
        print(f"Your current account balance is ${balance}")

        return balance

    def add_monthly_interest(self):
        interest = balance *  0.00083
        balance += interest

    
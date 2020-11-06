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
        amount = float(amount)

        self.balance += amount

        print(f"Amount Deposited: ${amount}")

    def withdrawl(self, amount):
        amount = float(amount)

        if amount > self.balance:
            print("Insufficient funds. You will be charged a $10 overdraft fee if you withdraw this amount. \
Do you wish to continue? (y/n) ")
            
            retry = True

            while retry:
                user_input = input()

                if user_input == 'y' or user_input == 'Y':
                    self.balance -= (amount + 10)
                    print(f"Withdraw confirmed, you have been charged a $10 overdraft fee. Amount Withdrawn: ${amount}")
                    retry = False
                elif user_input == 'n' or user_input == 'N':
                    "Withdraw canceled."
                    retry = False
                else:
                    print("Please type either 'y' or 'n'. Try again.")
        else:
            self.balance -= amount
            print(f"Amount Withdrawn: ${amount}")

    def get_balance(self):
        if  self.balance >= 0:
            print(f"Your current account balance is ${self.balance}")
        else:
            self.balance = self.balance * -1
            print(f"Your current account balance is -${self.balance}")

        return self.balance

    def add_monthly_interest(self):
        interest = self.balance *  0.00083
        self.balance += interest


restart = True

while restart:
    print("Welcome to your fictional bank account! To get started, enter your full name below:")

    users_name = str(input())

    account = BankAccount(users_name)

    def deposit():
        print("How much money would you like to deposit?")

        deposit_amount = input('$')

        account.deposit(deposit_amount)

    def withdrawl():
        print("How much money would you like to withdrawl?")

        withdrawl_amount = input('$')

        account.withdrawl(withdrawl_amount)

    def get_balance():
        account.get_balance()

    def add_monthly_interest():
        account.add_monthly_interest()

    menu = True

    while menu:
        print("\n\nChoose what you would like to do by typing in the number corresponding to your desired option. \n \
            1. Deposit \n \
            2. Withdrawl \n \
            3. Get your balance \n \
            4. View your current account receipt \n \
            5. Add monthly interest (ADMIN ONLY) \n \
            6. New account \n \
            7. Quit")

        user_choice = input() 

        if user_choice == "1":
            deposit()
        elif user_choice == "2":
            withdrawl()
        elif user_choice == "3":
            get_balance()
        elif user_choice == "5":
            add_monthly_interest()
        elif user_choice == "6":
            menu = False
        elif user_choice == "7":
            menu = False
            restart = False
        else:
            print("Please enter a valid option. Try again.")


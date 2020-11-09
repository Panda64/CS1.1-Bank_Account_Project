import random

# Function that generates a random 8-digit bank account number. Code is set up so that any number from 00000001 - 99999999 can 
# be displayed
def random_bank_account_number():
    num = random.randrange(1, 10000**2)
    num_with_zeros = '{:08}'.format(num)
    
    return num_with_zeros

# Function for hiding the first four digits of the bank account number (for simulated secruity purposes)
def hide_account_number(number):
    return "****" + number[4:]


class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name

    account_number = random_bank_account_number()
    routing_number = 123456789
    balance = 0

    def deposit(self, amount):
        amount = float(amount)

        self.balance += amount

        # Formatting the number so that only two decimal places are displayed at all times. This has been done multiple times
        # throughout this class
        amount = "{:.2f}".format(amount)

        print(f"Amount Deposited: ${amount}")

    def withdrawl(self, amount):
        amount = float(amount)

        # If the user tries to withdrawl an amount that is more than their current available balance, they will be prompted
        # for confirmation and informed that they will be charged a $10 overdraft fee
        if amount > self.balance:
            print("Insufficient funds. You will be charged a $10 overdraft fee if you withdraw this amount. \
Do you wish to continue? (y/n) ")
            
            retry = True

            while retry:
                user_input = input()

                if user_input == 'y' or user_input == 'Y':
                    self.balance -= (amount + 10)

                    amount = "{:.2f}".format(amount)

                    print(f"Withdraw confirmed, you have been charged a $10 overdraft fee. Amount Withdrawn: ${amount}")

                    retry = False
                elif user_input == 'n' or user_input == 'N':
                    print("Withdrawl canceled.")

                    retry = False
                else:
                    print("Please type either 'y' or 'n'. Try again.")    
        else:
            self.balance -= amount

            amount = "{:.2f}".format(amount)

            print(f"Amount Withdrawn: ${amount}")

    # Method for displaying the users current available balance. The following code ensures that if the users current available
    # balance is negative, it will proberly display the negative sign before the "$" symbol, not after. This is also done at 
    # the print_receipt method further down in this class
    def get_balance(self):
        if  self.balance >= 0:
            balance_display= "{:.2f}".format(self.balance)
            print(f"Your current account balance is ${balance_display}")
        else:
            positive_balance = self.balance * -1
            balance_display = "{:.2f}".format(positive_balance)
            print(f"Your current account balance is -${balance_display}")

        return self.balance

    def add_monthly_interest(self):
        interest = self.balance *  0.00083
        self.balance += interest
        print("1 month of interest has been added to your account.")

    def print_receipt(self):
        print(f" {self.full_name} \n \
Account No.: {hide_account_number(self.account_number)} \n \
Routing No.: {self.routing_number}")

        if self.balance >= 0:
            balance_display = "{:.2f}".format(self.balance)
            print(f" Balance: ${balance_display}")
        else:
            positive_balance = self.balance * -1
            balance_display = "{:.2f}".format(positive_balance)
            print(f" Balance: -${balance_display}")


# Instead of creating the three different object examples to test the methods and attributes, I created an interactive menu to 
# easily test everything from within the terminal
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

    def print_receipt():
        account.print_receipt()

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
        elif user_choice == "4":
            print_receipt()
        elif user_choice == "5":
            add_monthly_interest()
        elif user_choice == "6":
            menu = False
        elif user_choice == "7":
            menu = False
            restart = False
        else:
            print("Please enter a valid option. Try again.")


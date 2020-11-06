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

    


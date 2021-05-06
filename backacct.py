class InsufficientFunds(Exception):

    def __init__(self, acct_id, amt_attempted, current_bal):
        self.acct_id = acct_id
        self.amt_attempted = amt_attempted
        self.current_bal = current_bal

    def __str__(self):
        s = "Insufficent funds {:d}. " + " Attempted to withdraw ${:.2f} but only have {:.2f}"
        return s.format(self.acct_id, self.amt_attempted, self.current_bal)


class BankAccount:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0

    def __str__(self):
        s = str(self.id) + " " + str(self.first_name) + " " + str(self.last_name) + " " + " balance: $" + str(self.balance)
        return s

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFunds(self.id, amount, self.balance)
        self.balance -= amount

    def transfer_from(self, amount, to_account):
        self.withdraw(amount)
        to_account.deposit(amount)



def main():
    acct1 = BankAccount(123, "Joe", "Smith")
    print("acct1 BEFORE depost", acct1)
    acct1.deposit(100.00)
    print("acct1 AFTER deposit", acct1)
    acct1.deposit(200.00)
    print("acct1 AFTER second deposit", acct1)
    acct1.withdraw(50.00)
    print("acct1 AFTER first withdrawl", acct1)
    try:
        acct1.withdraw(1000.00)
    except InsufficientFunds as e:
        print(e)
    print(f"acct1 after second withdraw {acct1}")

    print()
    acct2 = BankAccount(345, "Jane", "Doe")
    print(f"Acct1 before transfer {acct1}")
    print(f"acct2 before transfer {acct2}")
    acct1.transfer_from(25.00, acct2)
    print(f"acct1 after transfer {acct1}")
    print(f"acct2 after transfer {acct2}")

    print()
    print(f"acct1 before bad transfer {acct1}")
    print(f"acct2 before bad transfer {acct2} ")
    try:
        acct1.transfer_from(10000.00, acct2)
    except InsufficientFunds as e:
        print(e)
    print(f"acct1 after bad transfer {acct1}")
    print(f"acct2 after bad transfer {acct2}")





main()

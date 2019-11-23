moneyTransfer = 1000


def wallet(balance, deposit1, withdraw1):
    def deposit():
        nonlocal balance
        balance += deposit1

    def withdraw():
        nonlocal balance
        if balance <= withdraw1:
            print("Cannot withdraw")
        else:
            balance -= withdraw1

    def show():
        print(balance)

    tu = {"name1": deposit, "name2": withdraw, "name3": show}
    return tu


Wallet1 = wallet(10000, 0, moneyTransfer)
Wallet2 = wallet(11000, moneyTransfer, 0)
Wallet1["name2"]()
Wallet2["name1"]()
Wallet1["name3"]()
Wallet2["name3"]()

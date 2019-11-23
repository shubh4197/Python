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

    tu = deposit, withdraw, show
    return tu


a, b, c = wallet(10000, 2000, 1000)
a()
c()

class InvalidCredential(Exception):
    def __init__(self, msg="Not found"):
        Exception.__init__(self, msg)


try:
    dict = {"Sachin": "ICC", "Saurav": "BCCI"}
    username = input("Enter username:")
    password = input("Enter password:")
    if username not in dict:
        raise InvalidCredential
    else:
        if dict[username] == password:
            print("success")
        else:
            raise InvalidCredential
except InvalidCredential as e:
    print(e)

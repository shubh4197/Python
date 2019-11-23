def demo():
    print("Hello World!")


test = demo()  # return of demo is passed

test1 = demo  # reference of demo is passed
print(type(test))
print(type(test1))


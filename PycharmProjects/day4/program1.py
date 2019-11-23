def outer(a):
    print("This is outer")

    def inner(*args, **kwargs):  # inner function should be generic
        print("This is inner")
        for i in args:
            if type(i) != str:
                print("Invalid")
                break
        else:
            for i in kwargs.values():
                if type(i) != str:
                    print("Invalid")
                    break
            else:
                a(*args, **kwargs)
        print("Inner finished")

    return inner


@outer
def hello(name):
    print("Hello" + name)


@outer
def sayhi(name1, name2):
    print("Hello1 " + name1 + " " + name2)


# hello = outer(hello)          This can be replaced by @wrapperfunctionname above the real function
# sayhi = outer(sayhi)          This can be replaced by @wrapperfunctionname above the real function
hello("Sachin")
sayhi(name1="Sachin", name2="Rahul")
hello(1)

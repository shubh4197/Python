# Closure-Where inner function is accessing data of the outer function and is being returned


def hello():
    count = 0

    def print1():
        nonlocal count
        count += 1
        print(count)

    return print1


outer = hello()
outer()
outer()
outer()

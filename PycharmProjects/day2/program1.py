def add(*args):
    print(type(args))
    print(args)
    sum1 = 0
    for x in args:
        sum1 += x
    print(sum1)


add(1, 2)
add(1, 2, 3)

print("Hello")

def add(**args):
    print(type(args), args)
    for i in args.values():
        print(i)

add(name1='Sachin')

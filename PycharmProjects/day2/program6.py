def outer():
    print("This is outer")

    def inner():
        print("This is inner")

    inner()


outer()

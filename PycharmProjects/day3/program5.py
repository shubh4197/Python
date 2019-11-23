class A:
    def sayhi(self):
        print("Hello A")


class B(A):
    def sayhi(self):
        print("Hello B")


class C(B, A):  # In case of multiple inheritence if the two parent class have parent child relationship then child
    # should be in the first position
    pass


obj = C()
obj.sayhi()

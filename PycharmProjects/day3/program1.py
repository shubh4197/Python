class Person:
    '''
    This is my first class
    '''
    team = "India"

    def sayhi(self):
        print("Hi all" + " " + self.fname + " " + self.lname)

    def __init__(self, f, l):
        self.fname = f
        self.lname = l

    def ___del__(self):
        print("Destructor called for " + self.fname + " " + self.lname)


obj = Person("Sachin", "Tendulkar")
setattr(obj, "pan", "CNIPD5639M")
print(getattr(obj, "pan"))
print(hasattr(obj, "pan"))
delattr(obj,"pan")
obj.team = "Australia"
obj.sayhi()
Person.sayhi(obj)
print(obj.__class__.__name__)
print(obj.__module__)
print(obj.__doc__)
print(obj.__dict__)
print(obj.fname, obj.team, obj.lname, obj.__class__.team)
del obj

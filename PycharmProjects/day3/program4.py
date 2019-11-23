class person:
    nationality = "India"

    def sayhi(self):
        print("Hi")

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class employee(person):
    org = "DXC"

    def __init__(self, fname, lname, dept, loc):  # Constructor Overriding from the parent class
        person.__init__(self, fname, lname)  # Constructor Chaining
        self.dept = dept
        self.loc = loc

    def work(self):
        print(self.fname)


class manager(employee):
    def __init__(self, fname, lname, dept, loc, array):
        employee.__init__(self, fname, lname, dept, loc)
        self.array = array

    def manage(self):
        print(self.fname + "is managing")

    def __str__(self):
        return "{fname} {lname} {dept}".format(**self.__dict__)

    def __bool__(self):
        return bool(self.fname) and bool(self.lname)

class student(person):
    institute = "Python University"

    def __init__(self, fname, lname, class1):  # Constructor Overriding from the parent class
        person.__init__(self, fname, lname)  # Constructor Chaining
        self.class1 = class1

    def study(self):
        print(self.fname + " " + "is studying")


e1 = manager("Shubham", "Das", "ECE", "NO", [])
e1.work()
e1.sayhi()
e1.manage()
e2 = student("Shubham", "Das", "12")
e2.study()
print(e2.nationality)
print(e1.org, e1.nationality)
# In case of multiple inheritence the first parent gets the first priority
print(str(e1))
print(bool(e1))

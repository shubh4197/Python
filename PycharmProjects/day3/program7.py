class Box:
    def __init__(self, itemlist):
        self.itemlist = itemlist

    def __str__(self):
        return str(self.itemlist)

    def __add__(self, other):
        return self.itemlist + other.itemlist

    def __lt__(self, other):
        return len(self.itemlist) < len(other.itemlist)


b1 = Box(["item1", "item2"])
b2 = Box(["item3", "item4", "item5"])
b3 = b1 + b2
print(b1)
print(b2)
print(b3)
print(b2 < b1)

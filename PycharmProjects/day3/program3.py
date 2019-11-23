class Product:
    def __init__(self, f, l, k):
        self.name = f
        self.brand = l
        self.cost = k

    def show(self):
        print("name={name},brand={brand},cost={cost}".format(**self.__dict__))


choice = int(input("Enter index"))
list2 = ["name", "brand", "cost"]
list1 = [Product("Jeans", "Spykar", 12), Product("Shirt", "Lee Cooper", 34), Product("Shoes", "Puma", 22)]

list1.sort(key=lambda el: getattr(el, list2[choice]))
for i in list1:
    i.show()

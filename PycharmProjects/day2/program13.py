obj = [
    {
        "pid": 12,
        "name": "Boat Rockerz 220",
        "cost": 1100,
        "brand": "Boat",
        "rating": 1,
        "category": "Electronics",
        "discount": 70
    },
    {
        "pid": 24,
        "name": "Acer Laptop",
        "cost": 40000,
        "brand": "Acer",
        "rating": 4,
        "category": "Electronics",
        "discount": 50
    },
    {
        "pid": 55,
        "name": "K20 pro",
        "cost": 27000,
        "brand": "Redmi",
        "rating": 4,
        "category": "Electronics",
        "discount": 90
    }

]
index = int(input("Enter the choice:"))
index4 = int(input("Should be in ascending or descending"))
list = ["cost", "rating", "discount"]
list3 = [False, True]
obj.sort(reverse=list3[index4], key=lambda el: el[list[index]])
print(obj)
index1 = int(input("Enter the choice:"))
list1 = ["brand", "name", "category"]
index2 = input("Enter the search:")
newobj = filter(lambda el: el[list1[index1]] == index2, obj)
for i in newobj:
    print("{name}:{brand}".format(**i))

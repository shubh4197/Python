num = int(input("Enter the number:"))
list1 = list(filter(lambda el: num % el == 0, range(1, num + 1)))
print(list1)

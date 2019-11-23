try:
    a=int(input("Enter number"))
    print(z)
    b=int(input("Enter number"))
    division=a/b
    print("data :",division)

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
print("Some other important tasks")
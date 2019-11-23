def sayhi(n1, n2, n3):
    print("Hi " + n1 + ' ' + n2 + ' ' + n3)


li = {"n1":"Sachin", "n2":"Saurav", "n3":"Rahul"}
sayhi(**li)

astring = "Hello World!"

print(len(astring))
print(astring.index("o"))
print(astring.index("o", 5))
print(astring.index("o", 5, 8))
print(astring.count("l"))
print(astring.upper())
print(astring.lower())
words = astring.split(" ")
print(words)
print(astring.startswith("Hello"))
print(astring.endswith("d!"))
print(astring.find("o"))
print(astring.find("o", 5, ))
print(astring.find("o", 5, 7))
print(astring.replace("World", "Python"))

data = "i am {0} from {1}"
sub1 = "string"
lang = "Python"
print(data.format(sub1, lang))

temp = " Hello {fname} {lname}, welcome  to {city}"
ob = [{
    "fname": "Rahul",
    "lname": "Dravid",
    "city": "Kolkata"
},
    {
        "fname": "Sachin",
        "lname": "Tendulkar",
        "city": "Bengaluru"
    },
    {
        "fname": "Saurav",
        "lname": "Ganguly",
        "city": "Bengaluru"
    }
]
for i in ob:
    dataString = temp.format(**i)
    print(dataString)



ob.sort(key=lambda el: el["fname"])
print(ob)


newobj = filter(lambda el: el["fname"].startswith('R'), ob)

for i in newobj:
    print("{fname} {lname} ".format(**i))

obj = [22, 32, 19, 43]



newobj = map(lambda el: 32 + el * 9 / 5, obj)
for i in newobj:
    print(i)

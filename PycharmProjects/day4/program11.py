# validate mobile number
import re

name=input("Enter phone")
pattern='^[0-9]{10}$'

if re.search(pattern,name):
     print("Validating")
else:
    print("Not validated")
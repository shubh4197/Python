import os.path
import os.path
file="C:/Users/amaheshwar24/Documents/pythontraining/chunks/demo.txt"
print("using", os.name,"C:/Users/amaheshwar24/Documents/pythontraining/chunks/demo.txt")
# print(os.path.splitext("C:/Users/amaheshwar24/Documents/pythontraining/chunks/demo.txt"))
# print(os.path.dirname("C:/Users/amaheshwar24/Documents/pythontraining/chunks/demo.txt"))
# print(os.path.basename("C:/Users/amaheshwar24/Documents/pythontraining/chunks/demo.txt"))
# print(os.path.exists(file))
print(os.path.islink(file))
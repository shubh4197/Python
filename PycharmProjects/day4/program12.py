import os.path
import re

# print(os.path.splitext("C:\Users\sdas300\PycharmProjects\demo.log"))
pattern = "^e[a-z]*"
os.chdir("C:\\Users\\sdas300\\PycharmProjects\\demo.log")
print(os.getcwd())
for i in os.listdir(os.getcwd()):
    if os.path.splitext(i)[1] == ".log" and os.path.isfile(i):
        fo = open(i, "rb")
        for line in fo:
            # print(line)
            match = re.search(pattern, line)
            if match:
                print(line)
        fo.close()

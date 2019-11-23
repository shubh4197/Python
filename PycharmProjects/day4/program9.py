import os.path
# print(os.path.splitext("C:\Users\sdas300\PycharmProjects\demo.log"))
os.chdir("C:\\Users\\sdas300\\PycharmProjects\\demo.log")
print(os.getcwd())
for i in os.listdir(os.getcwd()):
    if os.path.splitext(i)[1] ==".log" and os.path.isfile(i):
        fo=open(i,"rb")
        for line in fo:
            print(line)
        fo.close()
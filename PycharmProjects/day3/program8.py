with open('demo.txt', 'r') as fo:
    data = fo.readline()
    data1 = fo.readline()
    data2 = fo.readline()
    print(data)
    print(data1)
    print(data2)

fo = open('RA1511004010460 Shubham Das.jpg', 'rb')
i = 0
for line in fo:
    fo1 = open('chunks/demo' + str(i) + '.jpg', 'wb')
    print(line)
    i += 1
    fo1.write(line)
    fo1.close()
fo.close()

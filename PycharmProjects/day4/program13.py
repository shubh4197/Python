fin = open("demo.txt", "rt")
fout = open("out.txt", "wt")
li = ["vacation", "party", "outhouse"]
for line in fin:
    fout.write(line.replace('python', '******'))

fin.close()
fout.close()
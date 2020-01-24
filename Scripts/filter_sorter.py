#sorts by probability, used to work with external tools, deprecated
f = open("output112.txt", "r")
lines = f.readlines()
arr=[]
for line in lines[2:]:
    tmp = line[:-1].split('\t')
    if float(tmp[2]) <= 1:
        arr.append(line[:-1].split('\t'))
for e in arr:
    print(e)

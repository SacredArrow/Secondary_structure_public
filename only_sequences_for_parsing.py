import sys
if len(sys.argv) == 1:
    print("Path to file is essential!")
    exit(0)
in_file = sys.argv[1]
data = open(in_file).read().splitlines()
i = 0
id = 0
while i < len(data):
    # print(i, data[i])
    if (data[i].strip() == "" or data[i][0] == "#"):
        if "ID : " in data[i]:
            id = data[i].split(":")[1]
        i+=1
    else:
        seq = ""
        dot = ""
        while (data[i]!="" and data[i][0] in "GCAUgcau"):
            seq += data[i]
            i+=1
        if data[i] == "":
            i+=1
        while (i < len(data) and data[i].strip() != ""):
            dot+=data[i]
            i+=1
        print("> " + str(id))
        print(seq.upper())

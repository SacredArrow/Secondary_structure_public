names = ["ASE", "CRW", "PDB", "RFA", "TMR", "NDB", "SPR", "SRP" ] #PKB is different
id = 1
print("ID,Name,Source,Length,has_knots")
for name in names:
    f = open("RNA_" + name + ".txt", "r")
    lines = f.read().splitlines()
    i=0
    src = ""
    file = ""
    cnt = 0
    knot = True
    valid = True
    while(i<len(lines)):
        line = lines[i].strip(" ")
        if line == "" or line[0] == "#":
            if "External" in line:
                src = line.split(",")[0].split(":")[1].strip(" ")
            elif "File" in line:
                file = line.split(" ")[2].strip(" ")
            i+=1
            continue
        else:
            if line != "":
                for j in line:
                    if j not in "GCAUgcau":
                        valid = False
            i+=1
            line = lines[i]
            while (line == "" or line[0] not in ".()"):
                if line != "":
                    for j in line:
                        if j not in "GCAUgcau":
                            valid = False
                i+=1
                line = lines[i]
            while line != "":
                cnt+=len(line)
                for j in line:
                    if j not in ".()":
                        knot = False
                # print(cnt, line)
                # break
                i+=1
                if i < len(lines):
                    line = lines[i]
                else:
                    break
            if valid:
                print(id, file, src,cnt,0 if knot else 1, sep = ",")
            cnt = 0
            id+=1
            knot = True
            valid = True

f = open("RNA_PKB.txt", "r")
lines = f.read().splitlines()
for i in range(0, len(lines), 3):
    file = lines[i].split(":")[0].split(" ")[1]
    cnt = len(lines[i+1])
    print(id, file, "?", cnt, 1, sep = ",")
    id+=1

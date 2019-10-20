names = ["ASE", "CRW", "PDB", "RFA", "TMR", "NDB", "SPR", "SRP" ] #PKB is different
id = 1
print("ID,Name,Source,Length,has_knots")
decent_symbols = "GCAUgcau"
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
                if "Nucleic Acid Database" in src:
                    src = "Nucleic Acid Database"
                if "RCSB Protein Data Bank" in src:
                    src = "RCSB Protein Data Bank"
            elif "File" in line:
                file = line.split(" ")[2].strip(" ")
            i+=1
            continue
        else:
            if line != "":
                for j in line:
                    if j not in decent_symbols:
                        valid = False
            i+=1
            line = lines[i]
            while (line == "" or line[0] not in ".()"):
                if line != "":
                    for j in line:
                        if j not in decent_symbols:
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
                id+=1
            cnt = 0
            knot = True
            valid = True

f = open("RNA_PKB_old.txt", "r")
lines = f.read().splitlines()
for i in range(0, len(lines), 3):
    file = lines[i].split(":")[0].split(" ")[1]
    cnt = len(lines[i+1])
    valid = True
    for i in lines[i+1]:
        if i not in decent_symbols:
            valid = False
    if valid:
        print(id, file, "?", cnt, 1, sep = ",")
        id+=1

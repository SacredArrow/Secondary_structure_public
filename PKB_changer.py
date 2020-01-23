#normalises PKB
f = open("RNA_PKB_old.txt", "r")
lines = f.read().splitlines()
out = []
for ix, line in enumerate(lines):
    if line[0] == ">":
        if ix != 0 :
            out.append("")
        tmp = line.split(":")[0][2:]
        out.append("# File " + tmp)
        out.append("#" + line.split(":")[1])
        out.append("")
    else:
        out.append(line)
for line in out:
    print(line)

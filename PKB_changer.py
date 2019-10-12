#normalises PKB
f = open("RNA_PKB_old.txt", "r")
lines = f.read().splitlines()
out = []
for line in lines:
    if line[0] == ">":
        out.append("")
        tmp = line.split(":")[0][2:]
        out.append("# File:" + tmp)
        out.append("# " + line.split(":")[1])
    else:
        out.append(line)
for line in out:
    print(line)

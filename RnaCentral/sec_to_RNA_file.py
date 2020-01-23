base = open("RNA_CEN.txt", "r")
fasta = open("centroid_cleared.txt", "r")
out = open("../RNA_CEN.txt", "w")
fasta = fasta.read().splitlines()
ix = 2
base = base.read().splitlines()
for s in base:
    out.write(s + "\n")
    if not (s == "" or s[0] == "#"):
        out.write(fasta[ix] + "\n")
        ix+=3
        if ix > len(fasta):
            break

data = open("central.txt", "r").read().splitlines()
out = open("central.fasta", "w")
id = 1
for s in data:
    out.write("> " + str(id) + "\n")
    out.write(s + "\n")
    id+=1

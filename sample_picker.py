#picks data using csv
f = open("sample.csv", "r")
lines = f.read().splitlines()
lines = lines[1:]
lines = [x.split(",")[1] for x in lines]
f_out = open("sample_data.txt", "w")
for line in lines:
    bank = line.split("_")[0]
    if (bank [:3] == "PKB"):
        bank = "PKB"
    f = open("RNA_" + bank + ".txt", "r")
    bank_lines = f.read().splitlines()
    for i, s in enumerate(bank_lines):
        if line in s:
            while (bank_lines[i] != "" and bank_lines[i][0] == "#"):
                f_out.write(bank_lines[i] + "\n")
                i+=1
            while (i < len(bank_lines) and (bank_lines[i] == "" or bank_lines[i][0] != "#")):
                f_out.write(bank_lines[i] + "\n")
                i+=1

#picks data using csv
sets = ["train", "test", "validate"]
for set in sets:
    f = open(set + ".csv", "r")
    lines = f.read().splitlines()
    f.close()
    lines = lines[1:]
    lines = [(x.split(",")[0], x.split(",")[1]) for x in lines]
    f_out = open("sample_" + set +".txt", "w")
    for id, line  in lines:
        bank = line.split("_")[0]
        if (bank [:3] == "PKB"):
            bank = "PKB"
        f = open("RNA_" + bank + ".txt", "r")
        bank_lines = f.read().splitlines()
        f.close()
        for i, s in enumerate(bank_lines):
            if (line in s) and (bank != "PKB" or s.split(":")[1] == line):
                f_out.write("# ID : " + id + "\n")
                while (bank_lines[i] != "" and bank_lines[i][0] == "#"):
                    f_out.write(bank_lines[i] + "\n")
                    i+=1
                while (i < len(bank_lines) and (bank_lines[i] == "" or bank_lines[i][0] != "#")):
                    f_out.write(bank_lines[i] + "\n")
                    i+=1
    f_out.close()

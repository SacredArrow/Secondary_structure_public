#picks data using csv
def build_dict(bank):
    f = open("RNA_" + bank + ".txt", "r")
    bank_lines = f.read().splitlines()
    f.close()
    dict = {}
    for i, line in enumerate(bank_lines):
        if "# File " in line:
            dict.update({line.split(" ")[2] : i})
    return dict

sets = ["train", "test", "validate"]
banks = {}
# sets = ["validate"]
old_bank = ""
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
            # print(id, line)
        if ("_" not in line and bank !="PKB"):
            bank = "CEN"
        if (bank[:3] == "URS"): #TODO - make general
            bank = "CEN"
        if bank not in banks.keys():
            banks.update({bank : build_dict(bank)})
        if bank != old_bank:
            f = open("RNA_" + bank + ".txt", "r")
            bank_lines = f.read().splitlines()
        f_out.write("# ID : " + id + "\n")
        ix = banks[bank][line]
        for i in range(9):
            if ix + i < len(bank_lines):
                f_out.write(bank_lines[ix + i] + "\n")
        old_bank = bank
    f_out.close()
    #     # print(line)
    #     for i, s in enumerate(bank_lines):
    #         if (line in s) and (s.split(" ")[2] == line):
    #             f_out.write("# ID : " + id + "\n")
    #             while (bank_lines[i] != "" and bank_lines[i][0] == "#"):
    #                 f_out.write(bank_lines[i] + "\n")
    #                 i+=1
    #             while (i < len(bank_lines) and (bank_lines[i] == "" or bank_lines[i][0] != "#")):
    #                 f_out.write(bank_lines[i] + "\n")
    #                 i+=1
    #                 if i == len(bank_lines):
    #                     f_out.write("\n")
    #             break
    # f_out.close()

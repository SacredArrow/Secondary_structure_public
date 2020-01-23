# Picks data using csv
import sys

def build_dict(bank): # Makes dictionary from bank file, name:position
    f = open(banks_folder + "/RNA_" + bank + ".txt", "r")
    bank_lines = f.read().splitlines()
    f.close()
    dict = {}
    for i, line in enumerate(bank_lines):
        if "# File " in line:
            dict.update({line.split(" ")[2] : i})
    return dict

if len(sys.argv) != 4:
    print("Specify input folder, output folder and banks folder!")
    exit(0)

in_folder = sys.argv[1] # Full paths
out_folder = sys.argv[2]
banks_folder = sys.argv[3]
sets = ["train", "test", "validate"]
banks = {}
old_bank = "" # Performance causa
for set in sets:
    f = open(in_folder + "/" + set + ".csv", "r")
    lines = f.read().splitlines()
    f.close()
    lines = lines[1:]
    lines = [(x.split(",")[0], x.split(",")[1]) for x in lines] # Extract id and name
    f_out = open(out_folder + "/sample_" + set +".txt", "w")
    for id, line  in lines:
        bank = line.split("_")[0]
        if (bank [:3] == "PKB"):
            bank = "PKB"
        # if ("_" not in line and bank !="PKB"):
        #     bank = "CEN"
        if (bank[:3] == "URS"):
            bank = "CEN"
        if bank not in banks.keys():
            banks.update({bank : build_dict(bank)})
        if bank != old_bank:
            f = open(banks_folder + "/RNA_" + bank + ".txt", "r")
            bank_lines = f.read().splitlines()
        f_out.write("# ID : " + id + "\n")
        ix = banks[bank][line]
        for i in range(9): # Read all related lines
            if ix + i < len(bank_lines):
                f_out.write(bank_lines[ix + i] + "\n")
        old_bank = bank
    f_out.close()

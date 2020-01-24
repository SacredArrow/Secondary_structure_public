# Counts number of sequences in sample_xxx.txt files
import sys
file = open(sys.argv[1], "r").read().splitlines()
i = 0
cnt = 0
while i < len(file):
    if file[i][0] == "#":
        if "ID : " not in file[i]:
            print(file[i])
        cnt += 1
        while i < len(file) and (file[i] == "" or file[i][0] == "#"): # Skip other commented lines
            i += 1
        while i < len(file) and (file[i] == "" or file[i][0] != "#"): # Skip non-commented lines
            i += 1
print(cnt)

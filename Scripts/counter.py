#counts number of sequences in File
import sys
file = sys.argv[1]
f = open(file, "r")
cnt = 0
for line in f:
    if line[0] == "#": # 3 lines with "#" per sequence
        cnt+=1
print(cnt, cnt/3)

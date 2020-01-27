# Compares csv file and sample file. Used for debugging.
import sys
csv = open(sys.argv[1], "r").read().splitlines()
# for s in csv:
#     print(s)
csvs = list(map(lambda x: x.split(",")[0], csv))[1:]
# for s in csvs:
#     print(s)
# print(csvs)
sample =  open(sys.argv[2], "r").read().splitlines()
samples = []
for s in sample:
    if "# ID : " in s:
        samples.append(s.split(":")[1].strip())
print(len(csvs), len(samples))
print("in csv, not in sample")
for el in csvs:
    if el not in samples:
        print(el)
print("in sample, not in csv")
for el in samples:
    if el not in csvs:
        print(el)
print("Duplicates")
l = samples
print(set([x for x in l if l.count(x) > 1]))

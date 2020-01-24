# Generates stems
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("stem_length", help="Desired length of stem", type = int)
parser.add_argument("chain_length", help="Desired length of chain", type = int)
parser.add_argument("number_of_chains", help="Number of chains", type = int)
parser.add_argument("--loop_length", help="Size of a loop(more than 2 nucleotides in the real world). Default is 3", type = int, default = 3)
parser.add_argument("--stem_number", help="Number of stems. Default is 1", type = int, default = 1)
# parser.add_argument("--out_file", help="Path to the output. Default is \"./out.txt\"", default = "out.txt")
args = parser.parse_args()
structure_size = args.stem_length*2 + args.loop_length # = How many bases stem includes
if structure_size * args.stem_number >= args.chain_length:
    print("Can't fit stems!")
    exit(0)
out_file = "RNA_SYN" + str(args.stem_length)+".txt" # Name of file contains stem length
f = open(out_file, "w")
arr = [i for i in range(args.chain_length)]
# Can't place beginnig of structure in the end
arr = arr[:-structure_size] # or structure_size - 1
print(structure_size, arr)

def dive(positions, stems):
    res = []
    for ix, pos in enumerate(positions):
        new_positions = positions.copy() # Contains places, where we can start a loop
        new_stems = stems.copy()
        fst = []
        if ix - structure_size > 0: # If we pick a point, we can't start a loop in n bases before and n bases after, where n = structure_size
            fst = new_positions[:ix - structure_size]
        new_positions =  fst + new_positions[ix + structure_size:] # Cut bases, that can't be used now
        # print(ix, pos, new_positions)
        new_stems.append(pos)
        if len(new_stems) == args.stem_number:
            res.append(new_stems)
        else:
            for el in dive(new_positions, new_stems): # Recursion
                res.append(el)
    return res

res = dive(arr, [])
# print(res)
res = list(map(sorted, res)) # Sort everything

import itertools
res.sort()
res = list(k for k,_ in itertools.groupby(res)) # Only one value for every list
# print(res)

import random
res = random.sample(res, args.number_of_chains)
id = 1
for arr in res:
    s = ""
    i = 0
    f.write("# File SYN" + str(args.stem_length) + "_" + str(id) + "\n")
    f.write("# External source : Synthetic\n\n")
    while i < args.chain_length:
        if i in arr:
            curr = "G"
            for j in range(args.stem_length):
                f.write(curr)
                s+="("
                curr = "C" if curr == "G" else "G"
                i+=1
            for j in range(args.loop_length):
                f.write("A")
                s+="."
                i+=1
            for j in range(args.stem_length):
                f.write(curr)
                s+=")"
                curr = "C" if curr == "G" else "G"
                i+=1
        else:
            f.write("A")
            s+="."
            i+=1
    f.write("\n" + s + "\n\n")
    id+=1
f.close()

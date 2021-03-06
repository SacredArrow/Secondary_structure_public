from PIL import Image
import numpy as np
import sys
import os
#change here
in_file = sys.argv[1] #file with all samples info: id, seq, dot
out_dir_base = sys.argv[2]
if out_dir_base[-1] != "/":
    out_dir_base += "/"
out_dir = out_dir_base + "1/"
os.mkdir(out_dir)
size = 0
codes = {'A': 32, 'C': 64, 'G': 96, 'U': 128, 'T': 128}
cnt = 0
file_limit = 30000 # Used, because zip has problems with handling large amount of files in a directory

def process_sample(i_d, seq, dot):
    global out_dir, cnt
    pairs = {")" : "(", "}" : "{", "]" : "[", ">" : "<", "a" : "A", "b" : "B"} # Dot sequence pairs
    stack = []
    mtrx = []
    for i in range(len(dot)):
        if dot[i] == ".":
            continue
        else:
            paired = pairs.get(dot[i])
            if paired:
                j = len(stack) - 1
                while True:
                    if j < 0:
                        print("Pairing error!")
                        print(seq, dot)
                        exit(0)
                    if stack[j][1] == paired: # Found a pair
                        # print(stack[j][0], i)
                        mtrx.append((stack[j][0], i))
                        stack.pop(j)
                        break
                    else:
                        j-=1 # Pseudoknotes causa
            else:
                # print(dot[i], " not in pairs")
                stack.append((i, dot[i])) # Opening brackets go to stack
    if len(stack) != 0:
        print(i_d, seq,dot)
        print(stack)
        print("Error")
        exit(0)
    img = Image.new('L', (size, size), (0)) # Black background, white points
    pixels = np.array(img)
    for el in mtrx:
        x, y = el
        pixels[x][y] = 255
        #pixels[y][x] = 255 #for mirrored squares
    for i in range(len(seq)):
        pixels[i][i] = codes[seq[i]] #draw sequence at the diagonal
    Image.fromarray(pixels).save(out_dir + id + '.png')
    cnt += 1
    if cnt % file_limit == 0: # Split by folders
        out_dir = out_dir_base + str(cnt // file_limit + 1) + "/"
        os.mkdir(out_dir)




data = open(in_file).read().splitlines()
i = 0
id = 0
while i < len(data):
    # print(i, data[i])
    if (data[i].strip() == "" or data[i][0] == "#"):
        if data[i].strip() != "" and data[i][0] == "#":
            if "# ID :" in data[i]:
                id = data[i].split(":")[1].strip()
        i+=1
    else:
        seq = ""
        dot = ""
        while (data[i].strip() != "" and data[i][0] in "GCAUgcau"):
            seq += data[i]
            i+=1
        if data[i].strip() == "":
            i+=1
        while (i < len(data) and data[i].strip() != ""):
            dot+=data[i]
            i+=1
        size = len(seq)
        process_sample(id, seq.upper(), dot)

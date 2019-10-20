from PIL import Image
import numpy as np
import sys
#change here
in_file = sys.argv[1] #file with all samples info: id, seq, dot
out_dir = sys.argv[2]
if out_dir[-1] != "/":
    out_dir += "/"
size = 600
codes = {'A': 32, 'C': 64, 'G': 96, 'U': 128, 'T': 128}


def process_sample(i_d, seq, dot):
    pairs = {")" : "(", "}" : "{", "]" : "[", ">" : "<", "a" : "A"}
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
                        exit(0)
                    if stack[j][1] == paired:
                        # print(stack[j][0], i)
                        mtrx.append((stack[j][0], i))
                        stack.pop(j)
                        break
                    else:
                        j-=1
            else:
                # print(dot[i], " not in pairs")
                stack.append((i, dot[i]))
    if len(stack) != 0:
        print(stack)
        print("Error")
        exit(0)
    num = 1
    if len(seq) <=78:
        for k in range(3):
            for l in range(3):
                img = Image.new('L', (size, size), (0)) #black background, white points
                pixels = np.array(img)
                for el in mtrx:
                    x, y = el
                    pixels[x+k][y+l] = 255
                    #pixels[y][x] = 255 #for mirrored squares
                for i in range(len(seq)):
                    pixels[i+k][i+l] = codes[seq[i]] #draw sequence at the diagonal
                Image.fromarray(pixels).save(out_dir + id + "_" + str(num) + '.png')
                num+=1
                img = Image.new('L', (size, size), (0)) #black background, white points
                pixels = np.array(img)
                for el in mtrx:
                    x, y = el
                    pixels[len(seq)-(y+k) - 1][len(seq)-(x+l) - 1] = 255
                    #pixels[y][x] = 255 #for mirrored squares
                for i in range(len(seq)):
                    pixels[len(seq) - (i+k) - 1][len(seq) - (i+l) - 1] = codes[seq[i]] #draw sequence at the diagonal
                Image.fromarray(pixels).save(out_dir + id + "_" + str(num) + '.png')
                num+=1
    else:
        img = Image.new('L', (size, size), (0)) #black background, white points
        pixels = np.array(img)
        for el in mtrx:
            x, y = el
            pixels[x][y] = 255
            #pixels[y][x] = 255 #for mirrored squares
        for i in range(len(seq)):
            pixels[i][i] = codes[seq[i]] #draw sequence at the diagonal
        Image.fromarray(pixels).save(out_dir + id + "_" + str(num) + '.png')
        num+=1
        img = Image.new('L', (size, size), (0)) #black background, white points
        pixels = np.array(img)
        for el in mtrx:
            x, y = el
            pixels[len(seq)-(y)-1][len(seq)-(x)-1] = 255
            #pixels[y][x] = 255 #for mirrored squares
        for i in range(len(seq)):
            pixels[len(seq) - i-1][len(seq) - i-1] = codes[seq[i]] #draw sequence at the diagonal
        Image.fromarray(pixels).save(out_dir + id + "_" + str(num) + '.png')
        num+=1



data = open(in_file).read().splitlines()
i = 0
id = 0
while i < len(data):
    # print(i, data[i])
    if (data[i].strip() == "" or data[i][0] == "#"):
        if data[i].strip() != "" and data[i][0] == "#":
            if "# ID :" in data[i]:
                id = data[i].split(":")[1]
        i+=1
    else:
        seq = ""
        dot = ""
        while (data[i][0] in "GCAUgcau"):
            seq += data[i]
            i+=1
        while (i < len(data) and data[i].strip() != ""):
            dot+=data[i]
            i+=1
        process_sample(id, seq.upper(), dot)

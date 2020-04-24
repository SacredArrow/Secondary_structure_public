#Takes fasta and fasta from centroid and merges to bank file
from Bio import SeqIO
import sys
rna_path = sys.argv[1]
central_path = sys.argv[2]
no_black = True
records = list(SeqIO.parse(rna_path, "fasta"))
seconds = list(SeqIO.parse(central_path, "fasta"))
used_seqs = set()
for id in range(len(records)):
    is_black = True
    record = records[id]
    l = len(record.seq)
    if no_black:
        for el in seconds[id].seq[l:l+l]:
            if el != ".":
                is_black = False
    if (record.seq not in used_seqs) and not (no_black and is_black):
        # print(id)
        used_seqs.add(record.seq)

        print("# File",record.id)
        print("# External source : RNACentral")
        print("# Type : ?")
        print("# Length :", l)
        print("# Description :",' '.join(record.description.split(" ")[1:]))
        print()
        print(record.seq.transcribe())
        print(seconds[id].seq[l:l+l])
        print()

# print(len(records))
# print(records[0].seq)
# for record in records:
#     print(record)

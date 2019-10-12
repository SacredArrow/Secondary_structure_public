#helps count nucleotides
seq = "UAGUGUUUUUCGUUCCACUUAAAUCGAAACGAU"
dots = ":((((::::[[[[[[))))::::::]:]]]]]:"
for i in range(len(seq)):
    print((i+1)%10 if (i+1)%10!=0 else "|", end = "")
print()
print(seq)
print(dots)

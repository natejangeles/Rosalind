# Finding a motif in a DNA sequence
# python 9_DNA_Motif.py 9_Rosalind_Subs.txt

import sys

input_file = open(sys.argv[1], 'r')
dna_seq1 = input_file.readline().strip()
dna_seq2 = input_file.readline().strip()

i = 0
indices = []
# Iterates through a reference string dna_seq_1 and finds the indices at which
# the substring (motif) dna_seq_2 occurs. Uses 1-indexing to match DNA indexing.
last_index = len(dna_seq1) - len(dna_seq2) + 1 # last index to compare
for i in range(0,last_index):
    if dna_seq1[i:(i+len(dna_seq2))] == dna_seq2:
        indices.append(i+1)
    i = i + 1

# Prints each index separated by a space
print(" ".join(str(x) for x in indices))

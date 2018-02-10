# Determine the consensus string for a number of DNA sequences
# python 10_Consensus_String.py 10_Rosalind_Cons.txt

import sys
from helpers import rosalind_parser

seq_dict = rosalind_parser(sys.argv[1]) # sequence id, sequence dictionary
dna_seqs = [seqs for seq_id, seqs in seq_dict.items()] # list of L sequences

# Creates a list of n dictionaries with nucleotide counts at each position
# for all sequences. i.e. index 0 is a dict of A, C, T, G counts at position 0.
n = len(dna_seqs[0]) # length of each DNA sequence
base_matrix = []
for i in range(0,n):
    base_counts = {'A': 0, 'C': 0, 'G': 0 , 'T': 0}
    for seq in dna_seqs:
        nt = seq[i]
        base_counts[nt] += 1
    base_matrix.append(base_counts)

# Determine the most commonly occuring base at each position
s = ""
for base_count in base_matrix:
    target_value = max(base_count.values())
    for key,value in base_count.items():
        if value == target_value:
            s = s + key
            break
output_file = open("10_Rosalind_Out.txt", "w") # Prints the consensus sequence
output_file.write(s + "\n")

# Prints a nucleotide x position matrix where each cell holds the counts of that
# nucleotide at position p across all sequences.
for base in 'ACGT':
    s = base + ":"
    for base_count in base_matrix:
        s = s + " " + str(base_count[base])
    output_file.write(s + "\n")
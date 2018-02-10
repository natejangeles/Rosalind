# Counting DNA Nucleotides
# python 1_Nucleotides.py 1_Rosalind_DNA.txt

import sys

input_file = open(sys.argv[1], 'r')
dna_seq = input_file.readline().strip() # A single-line string

""" Returns a list containing the counts of A, C, G, and T 
    nucleotides in DNA string s. """
def nucleotideCounter(s):
	nt_dict = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 } 
	for nt in s: # Iterates through the string ONCE
		nt_dict[nt] = nt_dict[nt] + 1
	nt_counts = nt_dict.values()
	return nt_counts

nt_counts = nucleotideCounter(dna_seq)

# Print format meeting Rosalind specifications
print(' '.join(str(count) for count in nt_counts))

# Finding the reverse complement of a DNA sequence
# python 3_DNA_Complement.p 3_Rosalind_Revc 

import sys

input_file = open(sys.argv[1], 'r')
dna_seq = input_file.readline().strip() # A single-line text file

""" Given a DNA string s with at most 1000 bp, returns a string 
	representing the reverse complement, sc, of s. """
def reverseComplement(s):
	sc = ''
	complement_dict = { 'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	for nt in s[::-1]: # Iterate through DNA in reverse
		sc = sc + complement_dict[nt]
	return sc

rev_comp = reverseComplement(dna_seq)
print(rev_comp)

# Transcribing a DNA sequence into an RNA sequence
# python 2_Transcribe_DNA.py 2_Rosalind_DNA.txt
import sys

input_file = open(sys.argv[1], 'r')
dna_seq = input_file.readline().strip() # A single-line text file

""" Given a DNA string t with at most 1000 nucleotdies, returns a 
	string, rna, corresponding to the transcribed RNA sequence of t. """
def transcribeDNA(t):
	rna = t.replace('T', 'U')
	return rna

print(transcribeDNA(dna_seq))

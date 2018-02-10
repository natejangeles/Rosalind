# Compute the CG Content of various DNA strings in Rosalind FASTA format
# python 5_GC_Content.py 5_Rosalind_GC.txt
import sys

""" Calculates the CG content as a percentage for a DNA sequence. 
	PreCondition: seq is a DNA string. """
def gc_content(seq):
	gc_count = 0
	for nt in seq: # More efficient than using count()
		if nt == 'C' or nt == 'G':
			gc_count += 1
	gc_content = round( (gc_count/len(seq)) * 100, 6)
	return(gc_content)

with open(sys.argv[1], 'r') as inputFile:
	dna_dict = {}
	# Creates a dictionary with Sequence ID as keys, DNA sequence as values
	for line in inputFile:
		if line[0] == '>':
			seq_id = line[1:].strip("\n")
			dna_dict[seq_id] = ""
		else: 
			dna_dict[seq_id] += line.strip("\n")

	# Replaces the DNA sequence values with the corresponding CG content
	for seq_id in dna_dict:
		dna_dict[seq_id] = gc_content(dna_dict[seq_id])

	# Prints the ID and CG content of the sequence with the highest CG content
	target_value = max(dna_dict.values())
	for seq_id, cg_content in dna_dict.items():
		if cg_content == target_value:
			print(seq_id)
			print(cg_content)



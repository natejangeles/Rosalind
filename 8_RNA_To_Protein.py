# Convert an RNA String to a Protein String (Amino Acid Sequence)
# python 8_RNA_To_Protein.py 8_Rosalind_Prot.txt 8_AA_Dictionary.txt

import sys

def rna_to_protein(rna_string, aa_dict):
    """ 
    Returns the corresponding protein (amino acid) sequence of an RNA string.

    Parameter rna_string: The RNA sequence beginning with the start codon.
    Precondition: rna_string is a valid sequence at most 10 kbp long.

    Parameter aa_dict: The amino acid dictionary. 
    Precondition: A dictionary containing codon keys and corresponding AA values.
    """
    n = len(rna_string)
    protein_seq = ""
    for i in range(0,n,3):
        codon = rna_string[i:i+3]
        if aa_dict[codon] == "Stop":
            return(protein_seq)
        protein_seq = protein_seq + aa_dict[codon]
    return(protein_seq)

def construct_aa_dict(aa_file):
    """
    Returns a dictionary of codon, one-letter amino acid symbol pairs. 

    Parameter aa_file: Contains lines of codon, AA symbol pairs.
    Precondition: codon AA are separated by a space and pairs separated by tabs.
        e.g. UUU F      CUU L      AUU I      GUU V
    """
    aa_dict = {}
    with open(aa_file, 'r') as input_file:
        for line in input_file:
            line = line.split()
            for i in range(0, len(line)):
                if i % 2 == 0:
                    aa_dict[line[i]] = line[i+1]
    return(aa_dict)

with open(sys.argv[1], 'r') as seq_file:
    aa_dict = construct_aa_dict(sys.argv[2])
    rna_seq = seq_file.readline().strip()
    print(rna_to_protein(rna_seq, aa_dict))
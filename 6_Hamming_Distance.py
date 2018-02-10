# Calculates the number of differences in nucleotides between two DNA strings.
# python 6_Hamming_Distance.py 6_Rosalind_Hamm.txt
import sys 

""" Returns the number of point mutations between two DNA strings s and t.
    PreCondition: s and t are DNA strings of equal length n. """
def hamming_distance(s, t):
    n = len(s)
    count = 0
    for i in range(0, n):
        if s[i] is not t[i]:
            count += 1
    return count

with open(sys.argv[1], 'r') as inputFile:
    data = inputFile.readlines()
    dna_one = data[0].strip("\n")
    dna_two = data[1].strip("\n")
    hamm_dist = hamming_distance(dna_one, dna_two)
    print(hamm_dist)

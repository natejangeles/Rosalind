# Calculate basic probability of a genotype under Mendelian Inheritence
# python 7_Mendelian_Inheritance.py 7_Rosalind_IPRB.txt

import sys

""" Returns the probability that two randomly selected mating organisms will 
    produce an individual possessing a dominant allele. 

    PreCondition: Three positive integers k, m, and n, represent a population 
    containing k homozygous dominant, m heterozygous, and n homozygous 
    recessive organisms with (k+m+n) >= 2. """
def dominant_prob(k, m, n):
    total = float(k + m + n)
    prob_het_het = (m/total) * ((m-1)/(total-1))
    prob_het_rec = (m/total) * ((n)/(total-1)) + (n/total) * ((m)/(total-1))
    prob_rec_rec = (n/total) * ((n-1)/(total-1))
    return(1 - 0.25*prob_het_het - 0.5*prob_het_rec - prob_rec_rec)

with open(sys.argv[1], 'r') as inputFile:
    prob_list = inputFile.read().split(" ")
    prob_list = list(map(int, prob_list))
    k = prob_list[0]
    m = prob_list[1]
    n = prob_list[2]
    print(dominant_prob(k, m, n))

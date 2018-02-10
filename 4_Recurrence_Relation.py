# Rabbits and Recurrence Relation
# python 4_Recurrence_Relation.py 4_Rosalind_Fib.txt

import sys

""" Finds the n-th term of a sequence defined by a recurrence relation.
	The recurrence relation used is F_n = F_n-1 + k*F_n-2 with F_1 = F_2 = 1, 
	where F_n represent the number of rabbit pairs present after n months. 
	k represents the litter size of each reproducing rabbit pair. 
	i.e. Reproduction age is reach after two months and we assume each 
	rabbit pair successfully mates. """

""" Returns the value of the n_th term in the recurrence relation define above.
	PreCondition: 0 < n <= 40 and k <= 5, where n and k are integers. """ 
def WascallyRabbits(n, k):
	one_month_ago = 1
	two_months_ago = 1
	for month in range(2,n):
		this_month = one_month_ago + k*two_months_ago
		# Update F_n-1 and F_n-2 for the next F_n calculation
		two_months_ago = one_month_ago
		one_month_ago = this_month
	return this_month

input_file = open(sys.argv[1], 'r')

# Reads a txt file with one line containing two numbers separated by a space
input_params = input_file.readline().split(" ")
n = int(input_params[0])
k = int(input_params[1])

print(WascallyRabbits(n,k))

input_file.close()

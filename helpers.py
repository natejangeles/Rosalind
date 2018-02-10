def rosalind_parser(fasta_file):
    """
        Returns a dictionary of sequence id, sequence (key,value) pairs.

        Parameter fasta_file: A FASTA file containing the ids and sequences.
        Precondition: fasta_file is a Rosalind style FASTA, containing the
            read id prefaced by '>' and any number of lines following containing
            the correspodinding sequence.
    """
    with open(fasta_file, 'r') as input_file:
        seq_dict = {}
        for line in input_file:
            if line[0] == '>':
                seq_id = line[1:].strip()
                seq_dict[seq_id] = ""
            else:
                 seq_dict[seq_id] += line.strip()
        return(seq_dict) 
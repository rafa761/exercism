def to_rna(dna_strand):
    rna_dict = {'G': 'C',
                'C': 'G',
                'T': 'A',
                'A': 'U'}

    rna_strand = ''
    # Check if param is not empty
    if dna_strand:
        # Append result to rna_strand
        for strand in dna_strand:
            rna_strand += rna_dict[strand]
    return rna_strand

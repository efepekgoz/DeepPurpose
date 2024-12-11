def parse_fasta(fa):
    genes_and_seqs = {} 
    name, seq = None, []
    for line in fa:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                genes_and_seqs[name] = ''.join(seq)  
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        genes_and_seqs[name] = ''.join(seq)  
    return genes_and_seqs 

file_path = '/Users/efepekgoz/Project/toy_data/protein.faa'
with open(file_path, 'r') as file:
    genes_and_sequences = parse_fasta(file)

print(genes_and_sequences)
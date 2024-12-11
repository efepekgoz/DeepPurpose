"""def load_protein_all(protein_sequence, protein_name):
    # read all proteın sequences ınto a dıctıonary
    prots = {protein_name: protein_sequence}
    return prots"""

def read_protein_all(fa):
    name, seq = None, []
    for line in fa:
        line = line.rstrip()
        if line.startswith(">"):
            if name:
                yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name:
        yield (name, ''.join(seq))
file_path = '/Users/efepekgoz/Project/toy_data/protein.faa'
with open(file_path, 'r') as file:
    for gene, seq in read_protein_all(file):
        #print(gene, seq)
        pass

def extract_protein_by_name(prots, gene):
    return prots[gene], gene


my_protein_sequence = "MEEPQSDPSVEPPLSQETFSDLWKLLPENNVLSPLPSQAMDDLMLSPDDIEQWFTEDPGPDEAPRMPEAAPPVAPAPAAPTPAAPAPAPSWPLSSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKMFCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVVRRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFRHSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKGEPHHELPPGSTKRALPNNTSSSPQPKKKPLDGEYFTLQIRGRERFEMFRELNEALELKDAQAGKEPGGSRAHSSHLKSKKGQSTSRHKKLMFKTEGPDSD"


my_protein_name = "TP53_isoform_a"

prots = read_protein_all(my_protein_sequence, my_protein_name)

target, target_name = extract_protein_by_name(prots, my_protein_name)
print('The target is: ' + target)
print('The target name is: ' + target_name)
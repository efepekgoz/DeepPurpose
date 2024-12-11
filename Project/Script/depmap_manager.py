# codes for managing depmap's targets and mapping those targets to related sequences.

import pandas as pd

def create_new_csv_with_target(file_path='csv_files/colon_target.tsv', new_file_path='csv_files/colon_target_new.csv'):

    df = pd.read_csv(file_path, sep='\t', error_bad_lines=False)

    new_df = pd.DataFrame({
        'TARGET': df['TARGET'],
        'TARGET_SEQUENCE': ''
    })

    new_df.to_csv(new_file_path, index=False)
    print(f"New CSV file created at: {new_file_path}")

#create_new_csv_with_target()

from Bio import Entrez, SeqIO
file_path = 'csv_files/colon_target_new.csv'
df = pd.read_csv(file_path)
Entrez.email = "efe_pekgz@gmail.com"

def fetch_protein_sequence(gene_name):
# Fetch the protein sequence from NCBI for the given gene name
    try:
        handle = Entrez.esearch(db="protein", term=f"{gene_name}[Gene]", retmax=1)
        record = Entrez.read(handle)
        handle.close()
        
        if record["IdList"]:
            protein_id = record["IdList"][0]
            handle = Entrez.efetch(db="protein", id=protein_id, rettype="fasta", retmode="text")
            seq_record = SeqIO.read(handle, "fasta")
            handle.close()
            return str(seq_record.seq)
        else:
            return None
    except Exception as e:
        print(f"Error fetching sequence for {gene_name}: {e}")
        return None

df['TARGET_SEQUENCE'] = df['TARGET'].apply(fetch_protein_sequence)

updated_file_path = 'csv_files/colon_target_updated.csv'
df.to_csv(updated_file_path, index=False)

print(f"Updated CSV file saved to {updated_file_path}")


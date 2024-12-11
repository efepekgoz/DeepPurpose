import pandas as pd
import requests

# Function to fetch SMILES from PubChem using CID
def get_smiles(pubchem_id):
    base_url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound'
    url = f'{base_url}/cid/{pubchem_id}/property/CanonicalSMILES/JSON'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            smiles = data['PropertyTable']['Properties'][0]['CanonicalSMILES']
            return smiles
        else:
            print(f"Error fetching data: {response.status_code} - {response.reason}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

file_path = 'csv_files/cancerxgene_set2_raw.csv'  
df = pd.read_csv(file_path)

# Limit to the rows between 100 and 500
df_subset = df.iloc[5710:5720]

df_subset['smiles'] = df_subset['cid'].apply(lambda cid: get_smiles(cid) if pd.notnull(cid) else None).fillna(df_subset['smiles'])

df.update(df_subset)

modified_file_path = '/Users/efepekgoz/Project/csv_files/57ish.csv'  
df.to_csv(modified_file_path, index=False)

print(f"Modified CSV file saved to {modified_file_path}")

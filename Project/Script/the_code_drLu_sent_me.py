import requests

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
 
if __name__ == '__main__':
    pubchem_id = 2244  
    smiles = get_smiles(pubchem_id)
    if smiles:
        print(f"SMILES for PubChem Compound ID {pubchem_id}: {smiles}")
    else:
        print("Failed to retrieve SMILES.")
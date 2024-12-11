import pandas as pd

def create_new_csv(old_csv_path, new_csv_path):

    df = pd.read_csv(old_csv_path)

    new_df = pd.DataFrame()
    new_df['smiles'] = df['Drug Name']
    new_df['title'] = df['Drug Name'] + '_' + df['Cell Line Name']
    new_df['cid'] = df['Cosmic ID']
    
    new_df.to_csv(new_csv_path, index=False)
    
    print("New CSV created. The new CSV file is saved at:", new_csv_path)

def replace_spaces_with_underscores(new_csv_path):
    # Load the CSV file
    df = pd.read_csv(new_csv_path)
    
    # Replace spaces with underscores in specific columns
    df['smiles'] = df['smiles'].str.replace(' ', '_')
    df['title'] = df['title'].str.replace(' ', '_')

    # Save the modified DataFrame back to the CSV file
    df.to_csv(new_csv_path, index=False)
    
    print("Spaces replaced with underscores. The modified CSV file is saved at:", new_csv_path)


# Example usage:
old_csv_path = '/Users/efepekgoz/Downloads/cancerxgene_drugdata_set2.csv'
new_csv_path = '/Users/efepekgoz/Project/csv_files/cancerxgene_set2_raw.csv'

create_new_csv(old_csv_path, new_csv_path)
replace_spaces_with_underscores(new_csv_path)

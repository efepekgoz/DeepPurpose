import pandas as pd

csv_file = '/Users/efepekgoz/Project/csv_files/colon_target_updated.csv'
tab_file = '/Users/efepekgoz/Project/csv_files/broad.tab'

csv_data = pd.read_csv(csv_file)
tab_data = pd.read_csv(tab_file, delimiter='\t')

target_sequence = csv_data['TARGET_SEQUENCE']
target_name = csv_data['TARGET']
smiles = tab_data['smiles']
x_repurpose = tab_data['title']

combined_data = pd.DataFrame({
    'smiles': smiles,
    'TARGET_SEQUENCE': target_sequence,
    'X_repurpose': x_repurpose,
    'target_name': target_name
})

combined_data.to_csv('/Users/efepekgoz/Project/csv_files/broad_depmap_combined.csv', index=False)

print("New CSV file 'broad_depmap_combined.csv' created successfully.")

csv_file = '/Users/efepekgoz/Project/csv_files/colon_target_updated.csv'
tab_file = '/Users/efepekgoz/Project/csv_files/broad.tab'


csv_data = pd.read_csv(csv_file)
tab_data = pd.read_csv(tab_file, delimiter='\t')

target_sequence = csv_data['TARGET_SEQUENCE']
smiles = tab_data['smiles']

combined_data = pd.DataFrame({
    'SMILES': smiles,
    'Target Sequence': target_sequence
})

combined_data.to_csv('/Users/efepekgoz/Project/csv_files/broad_depmap_combined_twoColumns.csv', index=False)

print("New CSV file 'broad_depmap_combined.csv' created successfully.")

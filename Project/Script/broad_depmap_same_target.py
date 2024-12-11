import pandas as pd

# Load the CSV file
file_path = '/Users/efepekgoz/Project/csv_files/broad_depmap_combined.csv'  # Update with the correct path to your CSV file
df = pd.read_csv(file_path)

# Get the unique target names and their corresponding sequences
unique_targets = df['target_names'].unique()
target_sequences = {row['target_names']: row['Target Sequence'] for index, row in df.iterrows()}

# Save the filtered dataframes into separate CSV files with names like broad_depmap1, broad_depmap2, etc.
for i, target in enumerate(unique_targets, start=1):
    filtered_df = df[['SMILES', 'drug_names']].copy()
    filtered_df['Target Sequence'] = target_sequences[target]
    filtered_df['target_names'] = target
    file_name = f'broad_depmap{i}.csv'
    filtered_df.to_csv(file_name, index=False)

print("CSV files have been created successfully.")
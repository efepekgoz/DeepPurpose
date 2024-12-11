import pandas as pd
import os

# Load the TSV file
file_path = '/Users/efepekgoz/Project/csv_files/BDB_cleaned.tsv'
df = pd.read_csv(file_path, sep='\t')

output_file_path = '/Users/efepekgoz/Project/csv_files/BDB_text.txt'

df.to_csv(output_file_path, sep=' ', index=False)

print(f"File saved to {output_file_path}")

#code to map smiles strings and combine cancerxgene.org 's drug data

import pandas as pd
import os

# Path to the directory containing the CSV files
directory = '/Users/efepekgoz/Project/csv_files/'  # Update with the correct directory path if different

# List of CSV files
csv_files = [
    "0-3000.csv", "3000-5714.csv", "5714-9000.csv", "9000-12629.csv"
]

# Function to extract the row range from the filename
def extract_row_range(filename):
    base = os.path.basename(filename)
    range_str = base.replace(".csv", "")
    start, end = map(int, range_str.split("-"))
    return start, end

# DataFrame to store combined data
combined_df = pd.DataFrame()

# Loop through each file and concatenate the relevant rows
for file in csv_files:
    file_path = os.path.join(directory, file)
    start_row, end_row = extract_row_range(file)
    
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Select the rows based on the range
    df_selected = df.iloc[start_row:end_row + 1]
    
    # Append to the combined DataFrame
    combined_df = pd.concat([combined_df, df_selected], ignore_index=True)

# Save the combined DataFrame to a new CSV file
combined_csv_path = os.path.join(directory, "cancerxgene_set2.csv")
combined_df.to_csv(combined_csv_path, index=False)

print(f"Combined CSV file saved to {combined_csv_path}")

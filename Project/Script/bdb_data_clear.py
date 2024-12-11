import pandas as pd

def filter_tsv(input_file, output_file):

    df = pd.read_csv(input_file, sep='\t', error_bad_lines=False, warn_bad_lines=True)
    
    original_line_count = len(df)
    print(f"Number of lines in the original file: {original_line_count}")
    
    columns_to_keep = ['Ligand SMILES', 'BindingDB Target Chain Sequence', 'IC50 (nM)']
    filtered_df = df[columns_to_keep]
    
    filtered_line_count = len(filtered_df)
    print(f"Number of lines in the filtered file: {filtered_line_count}")
    
    filtered_df.to_csv(output_file, sep='\t', index=False)
    print(f"Filtered TSV file saved as {output_file}")

def remove_empty_ic50(input_file, output_file):

    #Function to remove rows with empty IC50 values from a TSV file and save the result to a new TSV file.

    df = pd.read_csv(input_file, sep='\t', error_bad_lines=False, warn_bad_lines=True)
    
    df_cleaned = df.dropna(subset=['IC50 (nM)'])
    
    df_cleaned.to_csv(output_file, sep='\t', index=False)
    print(f"TSV file with non-empty IC50 values saved as {output_file}")
    print("new line count:",len(df_cleaned))

# Example usage
input_file = '/Users/efepekgoz/Downloads/BindingDB_All_202408.tsv' 
output_file = '/Users/efepekgoz/Project/csv_files/BDB_filtered.tsv'  
cleaned_output_file = '/Users/efepekgoz/Project/csv_files/BDB_cleaned.tsv' 

#filter_tsv(input_file, output_file)
#remove_empty_ic50(output_file, cleaned_output_file)




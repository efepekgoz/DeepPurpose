import pandas as pd

def csv_to_txt_and_handle_duplicates(input_csv='/Users/efepekgoz/Project/csv_files/cancerxgene_set2.csv', output_txt='/Users/efepekgoz/Project/csv_files/repurpose.txt'):

    df = pd.read_csv(input_csv)

    duplicate_count = df.duplicated().sum()
    print(f'Number of duplicate rows: {duplicate_count}')

    df = df.drop_duplicates()

    formatted_df = df[['title', 'smiles']]

    formatted_df.to_csv(output_txt, sep=' ', index=False, header=False)

csv_to_txt_and_handle_duplicates()

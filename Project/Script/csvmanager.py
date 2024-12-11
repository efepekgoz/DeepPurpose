import pandas as pd


df = pd.read_csv("/Users/efepekgoz/Project/AID_171_datatable.csv")

df = df.dropna(subset=['PUBCHEM_CID'])
df  = df.dropna(subset=['PUBCHEM_SID'])

"""columns_to_convert = ['PUBCHEM_SID', 'PUBCHEM_CID', 'PUBCHEM_ACTIVITY_SCORE']
df[columns_to_convert] = df[columns_to_convert].astype(int)

"""
df.to_csv("modified_171.csv", index=False)

df_first = pd.read_csv("modified_171.csv")
df_second = pd.read_csv("/Users/efepekgoz/Project/Data/AID1706_training_conversions.csv")

df_new_rows = df_first[['PUBCHEM_CID', 'PUBCHEM_CID', 'PUBCHEM_EXT_DATASOURCE_SMILES']]
df_new_rows.columns = ['cid', 'title', 'smiles']  # Rename columns to match

df_appended = df_second.append(df_new_rows, ignore_index=True)

output_file = "modified_conversions.csv"
df_appended.to_csv(output_file, index=False)
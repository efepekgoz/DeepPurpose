import pandas as pd

original_csv = pd.read_csv('csv_files/mlh1_modified_conversions.csv')

new_csv = pd.read_csv('csv_files/AID_1117354_output.csv')

new_csv_selected = new_csv[['PUBCHEM_CID', 'title', 'PUBCHEM_EXT_DATASOURCE_SMILES']]
new_csv_selected.columns = ['cid', 'title', 'smiles']

appended_csv = original_csv.append(new_csv_selected, ignore_index=True)

appended_csv.to_csv('csv_files/jak2_modified_conversions.csv', index=False)

print("Data appended successfully and saved to 'appended.csv'.")

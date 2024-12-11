import pandas as pd
import numpy as np
import re
import math
import random
from rdkit import Chem
from rdkit.Chem import rdmolops

def txt_to_csv(input_file='/Users/efepekgoz/Project/csv_files/GDSC_all.tsv', output_file='/Users/efepekgoz/Project/csv_files/GDSC_all.tsv'):

    with open(input_file, 'r') as file:
        lines = file.readlines()

    data = []

    for line in lines:
        parts = line.strip().rsplit(',', 2)
        if len(parts) == 3:
            drug = parts[0]
            target = parts[1]
            binding_score = parts[2]
            data.append([drug, target, binding_score])
        else:
            print(f"Skipping malformed line: {line.strip()}")

    df = pd.DataFrame(data, columns=['drug', 'target', 'binding score'])
    df.to_csv(output_file, index=False)

    print(f"Data has been successfully converted to {output_file}")

#txt_to_csv()

def remove_duplicates_and_round_floats(input_file, output_file):
    seen_lines = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Split the line into text and float parts
            *text_parts, float_part = line.rsplit(' ', 1)
            # Convert the float part to a float, round it, and format it
            rounded_float = f"{float(float_part.strip()):.3f}"
            new_line = ' '.join(text_parts + [rounded_float])
            # Check if the new line is already seen
            if new_line not in seen_lines:
                outfile.write(new_line + '\n')
                seen_lines.add(new_line)

#remove_duplicates_and_round_floats('/Users/efepekgoz/Project/csv_files/GDSC_text_colon.txt', '/Users/efepekgoz/Project/csv_files/GDSC_text_unique.txt')

def convert_ic50_to_binary(input_file, output_file, threshold=100):
    seen_lines = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            *text_parts, float_part = line.rsplit(' ', 1)
            ic50_value = float(float_part.strip())
            binary_value = '1' if ic50_value < threshold else '0'
            new_line = ' '.join(text_parts + [binary_value])
            if new_line not in seen_lines:
                outfile.write(new_line + '\n')
                seen_lines.add(new_line)

#convert_ic50_to_binary('/Users/efepekgoz/Project/csv_files/GDSC_text_unique.txt', '/Users/efepekgoz/Project/csv_files/GDSC_text_binary.txt')

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        if len(line) > 30:
            main_part = line[:-30]
            last_part = line[-30:]
            last_part = last_part.replace('"', '').replace('<', '').replace('>', '')
            processed_line = main_part + last_part
        else:
            processed_line = line.replace('"', '').replace('<', '').replace('>', '')
        processed_lines.append(processed_line)
    
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)

#process_file('/Users/efepekgoz/Project/csv_files/BDB_text.txt', '/Users/efepekgoz/Project/csv_files/BDB_clean_text.txt')

def remove_extra_space_before_number(input_file, output_file):
    import re

    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        # regex for  multiple spaces before a number at the end of the line
        processed_line = re.sub(r'(\s+)(\d+(\.\d+)?)$', r' \2', line)
        processed_lines.append(processed_line)
    
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)

#remove_extra_space_before_number('/Users/efepekgoz/Project/csv_files/BDB_clean_text.txt', '/Users/efepekgoz/Project/csv_files/BDB_spaced_text.txt')

def remove_lines_not_ending_with_number(input_file, output_file):

    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    processed_lines = []
    for line in lines:
        # regex for lines taht end with a number
        if re.search(r'\d+(\.\d+)?$', line.strip()):
            processed_lines.append(line)
    
    with open(output_file, 'w') as file:
        file.writelines(processed_lines)

#remove_lines_not_ending_with_number('/Users/efepekgoz/Project/csv_files/BDB_spaced_text.txt', '/Users/efepekgoz/Project/csv_files/BDB_clean_spaced.txt')

def convert_ic50_to_logspace(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:

            *text_parts, float_part = line.rsplit(' ', 1)
            ic50_value = float(float_part.strip())
            # Convert the IC50 value to logspace (nM -> p)
            log_ic50_value = -np.log10(ic50_value) + 9
            # Format the log IC50 value to 3 decimal places
            formatted_log_ic50 = f"{log_ic50_value:.3f}"
            new_line = ' '.join(text_parts + [formatted_log_ic50])
            outfile.write(new_line + '\n')

#convert_ic50_to_logspace('/Users/efepekgoz/Project/csv_files/BDB_clean_spaced.txt', '/Users/efepekgoz/Project/csv_files/BDB_logspace.txt')

def remove_lines_with_non_positive_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            
            try:
                *text_parts, number_part = line.rsplit(' ', 1)
                number_value = float(number_part.strip())
                
                if number_value > 0:
                    outfile.write(line + '\n')
            except ValueError:
                continue

#remove_lines_with_non_positive_numbers('/Users/efepekgoz/Project/csv_files/BDB_clean_spaced.txt', '/Users/efepekgoz/Project/csv_files/BDB_positive.txt')

def convert_ic50_to_logspace(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line_number, line in enumerate(infile, 1):
            line = line.strip()
            if not line:
                continue
            
            try:
                *text_parts, float_part = line.rsplit(' ', 1)
                ic50_value = float(float_part.strip())
                
                if ic50_value > 0:
                    log_ic50_value = -np.log10(ic50_value) + 9
                    formatted_log_ic50 = f"{log_ic50_value:.3f}"
                else:
                    formatted_log_ic50 = 'inf'  #or some other placeholder indicating invalid IC50 value
                    print(f"Error on line {line_number}: IC50 value is zero or negative.")
                
                new_line = ' '.join(text_parts + [formatted_log_ic50])
                outfile.write(new_line + '\n')
            except ValueError:
                print(f"Error on line {line_number}: Could not convert to float: {float_part}")
                continue

#convert_ic50_to_logspace('/Users/efepekgoz/Project/csv_files/BDB_positive.txt', '/Users/efepekgoz/Project/csv_files/BDB_logspace.txt')

def randomize_and_save_first(input_file, output_file, num_lines_to_save=500000):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    random.shuffle(lines)
    
    # Get the first 400,000 lines (or fewer if there are not enough lines)
    lines_to_save = lines[:num_lines_to_save]
    
    # Write the first 400,000 lines to the new output file
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines_to_save)


#randomize_and_save_first('/Users/efepekgoz/Project/csv_files/BDB_log_fixed.txt', '/Users/efepekgoz/Project/csv_files/BDB_random_500k.txt')

def combine_files(input_file1, input_file2, output_file):
    with open(input_file1, 'r') as infile1:
        lines1 = infile1.readlines()

    with open(input_file2, 'r') as infile2:
        lines2 = infile2.readlines()
    
    combined_lines = lines1 + lines2
    random.shuffle(combined_lines)

    with open(output_file, 'w') as outfile:
        outfile.writelines(combined_lines)

#500k-89k + 190kgdsc
input_file1 = '/Users/efepekgoz/Project/csv_files/BDB_valid_500k.txt'
input_file2 = '/Users/efepekgoz/Project/csv_files/GDSC2_text_logspace.txt'
output_file = '/Users/efepekgoz/Project/csv_files/BDB_GDSC2_500k.txt'
combine_files(input_file1, input_file2, output_file)


def find_longest_smiles(input_file='/Users/efepekgoz/Project/csv_files/GDSC2_text_logspace.txt'):
    longest_smiles = ""
    longest_length = 0

    with open(input_file, 'r') as infile:
        for line in infile:
            smiles = line.split(' ')[0]  # Extract SMILES string
            if len(smiles) > longest_length:
                longest_smiles = smiles
                longest_length = len(smiles)
    
    print(f"The longest SMILES string is: {longest_smiles}")
    print(f"Length of the longest SMILES string: {longest_length}")

#print("finding the longest smiles...")
#find_longest_smiles()

def delete_long_smiles_lines(input_file, output_file, max_length=133):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.split(' ', 1)  # Split only at the first space
            if len(parts) < 2:
                continue  # Skip lines that do not have both SMILES and target sequence
            
            smiles, target_sequence = parts[0], parts[1]
            if len(smiles) <= max_length and target_sequence.strip().startswith('M'):
                outfile.write(line)

#print("removing long smiles from BDB...")
#delete_long_smiles_lines('/Users/efepekgoz/Project/csv_files/BDB_logspace_cleaned.txt', '/Users/efepekgoz/Project/csv_files/BDB_short_clean.txt')

def check_and_filter_file(input_file, output_file):
    invalid_lines = 0

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            line_number = 0
            for line in infile:
                line_number += 1
                values = line.split()
                
                # Check if the line has exactly three parts
                if len(values) != 3:
                    print(f"Invalid format at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue
                
                smiles, target_sequence, ic50_value = values
                
                # Check if the IC50 value is a valid float
                try:
                    float(ic50_value)
                except ValueError:
                    print(f"Invalid IC50 value at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue
                
                outfile.write(line)
        
        print(f"File validation completed. Number of invalid lines: {invalid_lines}")
    except FileNotFoundError:
        print('Path Not Found, please double check!')


#check_and_filter_file('/Users/efepekgoz/Project/csv_files/BDB_logspace.txt', '/Users/efepekgoz/Project/csv_files/BDB_log_fixed.txt')


def clean_dataset(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    original_num_lines = len(lines)
    valid_lines = []
    
    for idx, line in enumerate(lines):
        values = line.strip().split()
        if len(values) == 3:
            valid_lines.append(line)
        else:
            print(f"Invalid line {idx + 1}: {line.strip()}")

    with open(output_file, 'w') as f:
        f.writelines(valid_lines)
    
    output_num_lines = len(valid_lines)
    print(f"Original number of lines: {original_num_lines}")
    print(f"Number of lines in the output file: {output_num_lines}")

#clean_dataset('/Users/efepekgoz/Project/csv_files/BDB_GDSC2_400k.txt', '/Users/efepekgoz/Project/csv_files/BDB_GDSC2_400k_clean.txt')


#The number of rows in the input file is: 152148
#The number of rows in the output file is: 139122

def check_smiles_validity(smiles):
    try:
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return False, 0
        # Attempt to Kekulize the molecule
        try:
            Chem.Kekulize(mol)
        except:
            return False, 0        
        # Check for explicit valence errors
        for atom in mol.GetAtoms():
            if atom.GetExplicitValence() > Chem.GetPeriodicTable().GetDefaultValence(atom.GetAtomicNum()):
                return False, 0
                
        num_atoms = mol.GetNumAtoms()
        return True, num_atoms
    except Exception as e:
        print(f"Error processing SMILES {smiles}: {e}")
        return False, 0

def filter_invalid_smiles(input_file, output_file, max_atoms=100):
    invalid_lines = 0

    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            line_number = 0
            for line in infile:
                line_number += 1
                print(f"Processing line {line_number}...")
                values = line.split()
                
                if len(values) != 3:
                    print(f"Invalid format at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue
                
                smiles, target_sequence, ic50_value = values
                
                try:
                    float(ic50_value)
                except ValueError:
                    print(f"Invalid IC50 value at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue
                
                # Check if the SMILES string is valid and has an acceptable number of atoms
                is_valid, num_atoms = check_smiles_validity(smiles)
                if not is_valid:
                    print(f"Invalid SMILES at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue
                
                if num_atoms > max_atoms:
                    print(f"SMILES with more than {max_atoms} atoms at line {line_number}: {line.strip()}")
                    invalid_lines += 1
                    continue

                outfile.write(line)
        
        print(f"File validation completed. Number of invalid lines: {invalid_lines}")
    except FileNotFoundError:
        print('Path Not Found, please double check!')

"""
input_file = '/Users/efepekgoz/Project/csv_files/BDB_random_500k.txt'
output_file = '/Users/efepekgoz/Project/csv_files/BDB_valid_500k.txt'
filter_invalid_smiles(input_file, output_file)
"""

def randomize_and_extract(input_file_path, output_file_path, num_lines=200000):
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()

        random.shuffle(lines)

        selected_lines = lines[:num_lines]

        with open(output_file_path, 'w') as file:
            file.writelines(selected_lines)

        print(f"Successfully created {output_file_path} with {num_lines} random lines.")
    except Exception as e:
        print(f"An error occurred: {e}")

#randomize_and_extract('/Users/efepekgoz/Project/csv_files/BDB_GDSC2_500k.txt', '/Users/efepekgoz/Project/csv_files/subset200k.txt')

def clean_aid171(filename):

  df = pd.read_csv(filename)

  df = df.dropna(subset=["PUBCHEM_CID", "PUBCHEM_EXT_DATASOURCE_SMILES"])

  return df


cleaned_df = clean_aid171("/Users/efepekgoz/Project/csv_files/AID_171_datatable.csv")
cleaned_df.to_csv("/Users/efepekgoz/Project/csv_files/AID_171_clean.csv", index=False)
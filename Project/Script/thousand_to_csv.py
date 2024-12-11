import os
import csv

# Initialize lists to hold the extracted data
ranks = []
drug_names = []
target_names = []
binding_scores = []

# Iterate through all 1000 folders
for i in range(1, 1001):
    folder_name = f'save_folder{i}'
    file_path = os.path.join(folder_name, 'results_aggregation', 'virtual_screening.txt')
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()        
        # Process each line to extract the data
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith('|  ') and '|' in line:
                parts = line.split('|')
                rank = parts[1].strip()
                drug_name = parts[2].strip()
                target_name = parts[3].strip()
                binding_score = parts[4].strip()
                
                ranks.append(rank)
                drug_names.append(drug_name)
                target_names.append(target_name)
                binding_scores.append(binding_score)

# Write the extracted data to a single CSV file
with open('thousand_combined_virtual_screening.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Rank', 'Drug Name', 'Target Name', 'Binding Score'])
    for i in range(len(ranks)):
        csvwriter.writerow([ranks[i], drug_names[i], target_names[i], binding_scores[i]])

print("Combined CSV file created successfully.")

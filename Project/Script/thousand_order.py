#Sorting the thousand loop run's result and then removing duplicates.
#
import csv

def sort_by_binding_score(input_csv='csv_files/thousand_combined_virtual_screening.csv', output_csv='csv_files/sorted_virtual_screening.csv'):
    with open(input_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        data = list(csvreader)

    data.sort(key=lambda x: float(x[3]))

    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(data)

    print(f"Data sorted by Binding Score and saved to {output_csv}")


def remove_duplicates(input_csv='csv_files/sorted_virtual_screening.csv', output_csv='csv_files/unique_sorted_virtual_screening.csv'):
    with open(input_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        data = list(csvreader)

    # Remove duplicates based on Drug Name and Target Name
    seen = set()
    unique_data = []
    for row in data:
        drug_target_combo = (row[1], row[2])  # Tuple of (Drug Name, Target Name)
        if drug_target_combo not in seen:
            seen.add(drug_target_combo)
            unique_data.append(row)

    with open(output_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        csvwriter.writerows(unique_data)

    print(f"Duplicates removed and data saved to {output_csv}")


sort_by_binding_score()
remove_duplicates()
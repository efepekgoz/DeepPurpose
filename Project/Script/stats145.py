import re
from collections import Counter

def extract_drugs(text):
    # Regex to match the drug names in the format they appear in the document
    drug_pattern = re.compile(r'\|\s+\d+\s+\|\s+(.*?)\s+\|')
    return drug_pattern.findall(text)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    file_path = '/Users/efepekgoz/Project/csv_files/145textresults.rtf'
    content = read_file(file_path)

    drugs = extract_drugs(content)

    drug_counts = Counter(drugs)

    sorted_drugs = drug_counts.most_common()

    for drug, count in sorted_drugs:
        print(f'{drug}: {count}')

if __name__ == "__main__":
    main()

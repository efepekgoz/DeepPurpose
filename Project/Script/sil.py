def remove_duplicate_rows(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Use a set to keep track of unique lines
    unique_lines = set(lines)
    
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

input_file = '/Users/efepekgoz/my_virt_screening_results.txt'
output_file = '/Users/efepekgoz/output_virt.txt'
remove_duplicate_rows(input_file, output_file)

def count_lines_in_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)


number_of_lines = count_lines_in_file(input_file)
print(f'The number of rows in the input file is: {number_of_lines}')
number_of_lines = count_lines_in_file(output_file)
print(f'The number of rows in the output file is: {number_of_lines}')

def sort_file_by_floats(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    lines_with_numbers = []
    for line in lines:
        try:
            number = float(line.strip().split(',')[-1])
            lines_with_numbers.append((line, number))
        except ValueError:
            print(f"Skipping line: {line.strip()} - No valid float found at the end")

    sorted_lines_with_numbers = sorted(lines_with_numbers, key=lambda x: x[1])

    with open(output_file, 'w') as file:
        for line, number in sorted_lines_with_numbers:
            file.write(line)

#input_file = 'input.txt'
input_file = output_file
output_file = 'sorted_output.txt'
sort_file_by_floats(input_file, output_file)

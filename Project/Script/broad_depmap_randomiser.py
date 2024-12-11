import pandas as pd
import random

# Read the CSV file
df = pd.read_csv('/Users/efepekgoz/Project/csv_files/broad_depmap_combined_repeat.csv')

# Generate the list of numbers from 1 to 6111 and shuffle them
random_numbers = list(range(6111))
random.shuffle(random_numbers)

# Move columns 1 and 3 according to the randomized list
df['Column1_Shuffled'] = df.iloc[random_numbers, 0].values
df['Column3_Shuffled'] = df.iloc[random_numbers, 2].values

# Replace original columns with shuffled columns
df.iloc[:, 0] = df['Column1_Shuffled']
df.iloc[:, 2] = df['Column3_Shuffled']

# Drop the temporary shuffled columns
df.drop(columns=['Column1_Shuffled', 'Column3_Shuffled'], inplace=True)

# Save the modified DataFrame to a new CSV file
df.to_csv('/Users/efepekgoz/Project/csv_files/shuffled_file.csv', index=False)

print("Columns 1 and 3 have been shuffled and saved to 'shuffled_file.csv'.")

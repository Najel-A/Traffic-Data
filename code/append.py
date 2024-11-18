import pandas as pd

# List of file paths for the three years
file_paths = ['updated_2021_file.csv', 'updated_2022_file.csv', 'updated_2023_file.csv']

# Step 1: Read and append all files into one DataFrame
combined_df = pd.concat([pd.read_csv(file) for file in file_paths], ignore_index=True)

# Step 2: Save the combined data into a new CSV file
combined_df.to_csv('combined_2021_2023_data.csv', index=False)

# Optional: Print a sample to verify
print(combined_df.head())
print(combined_df.tail())
print(combined_df.info())

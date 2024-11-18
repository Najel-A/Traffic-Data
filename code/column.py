import pandas as pd

file_paths = ['updated_2021_file.csv', 'updated_2022_file.csv', 'updated_2023_file.csv']

combined_df = pd.concat([pd.read_csv(file) for file in file_paths], ignore_index=True)

# Filter to keep only rows where station_id is 49090
filtered_df = combined_df[combined_df['station_id'] == 49090]

filtered_df.to_csv('filtered_combined_2021_2023_data.csv', index=False)

print(filtered_df.head())
print(filtered_df.info())

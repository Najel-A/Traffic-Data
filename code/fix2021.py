import pandas as pd


file_path = 'fixed_combined_cleaned_2021_traffic_data.csv'
df = pd.read_csv(file_path)

df['year_record'] = 2021

df.to_csv(file_path, index=False)

print(f"The file '{file_path}' has been updated successfully!")

import pandas as pd
# convert to date type

file_path = "unique_merged_table.csv"  
data = pd.read_csv(file_path)


data['date'] = pd.to_datetime(data['date'], errors='coerce')


if data['date'].isnull().any():
    print("Some values in 'date' could not be converted to a valid date.")


output_path = "updated_unique_merged_table_latest.csv"  
data.to_csv(output_path, index=False)

print("date has been converted to date type and saved to a new file.")
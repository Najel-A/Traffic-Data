import pandas as pd

# Load the dataset
file_path = "updated_unique_merged_table_latest.csv"  # Replace with your file path
date_column = "date"  # Replace with your date column name

# Read the CSV file
df = pd.read_csv(file_path)

# Ensure the date column is in datetime format
df[date_column] = pd.to_datetime(df[date_column])

# Define the expected date range from February 2021 to December 2023
start_date = "2021-02-01"
end_date = "2023-12-31"
full_date_range = pd.date_range(start=start_date, end=end_date)

# Identify missing dates
missing_dates = full_date_range.difference(df[date_column])

# Output missing dates
if not missing_dates.empty:
    print("Missing Dates:")
    print(missing_dates)
else:
    print("No missing dates in the dataset.")
    print(df.length)

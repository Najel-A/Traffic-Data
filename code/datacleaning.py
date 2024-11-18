import pandas as pd
import numpy as np

csv_file_path = 'combined_2023_traffic_data.csv'

df = pd.read_csv(csv_file_path)

df.rename(columns={'year_record': 'year', 'month_record': 'month', 'day_record': 'day'}, inplace=True)
df['date'] = pd.to_datetime(df[['year', 'month', 'day']]).dt.strftime('%m/%d/%Y')

df.drop(columns=['year', 'month', 'day'], inplace=True)


float_columns = df.select_dtypes(include='float64').columns
if not float_columns.empty:
    # Replace non-finite values with 0 before conversion
    df[float_columns] = df[float_columns].replace([np.inf, -np.inf], np.nan).fillna(0)
    # Convert to int64
    df[float_columns] = df[float_columns].astype('int64')

column_to_move = 'date'
first_column = df.pop(column_to_move)
df.insert(0, column_to_move, first_column)

df.to_csv('updated_2023_file.csv', index=False)

print(df.head())
print(df.dtypes)

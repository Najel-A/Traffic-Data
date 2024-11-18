import pandas as pd

df = pd.read_csv('filtered_combined_2021_2023_data.csv')  

df['date'] = pd.to_datetime(df['date'], errors='coerce') 

print(df.dtypes)

# Melt the dataframe to convert the hour columns into a long format
df_long = pd.melt(
    df, 
    id_vars=['date', 'record_type', 'state_code', 'f_system', 'station_id', 
             'travel_dir', 'travel_lane', 'day_of_week', 'restrictions'], 
    value_vars=[f'hour_{i:02}' for i in range(24)],  # Fixed column names to match 'hour_00', 'hour_01', etc.
    var_name='hour', 
    value_name='value'
)


df_long['hour'] = df_long['hour'].str.extract('(\d+)').astype(int)

print(df_long.dtypes)

df_long.to_csv('traffic_data_hour_fixed.csv', index=False)  

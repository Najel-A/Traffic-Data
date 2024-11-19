import pandas as pd
#Used Chatgpt for logic
df = pd.read_csv('combined_cleaned_2021-2023_traffic_data.csv') 


df_long = pd.melt(df, 
                  id_vars=['date','station_id', 
                           'travel_dir', 'travel_lane', 'day_of_week'], 
                  value_vars=[f'hour_{i:02}' for i in range(24)], 
                  var_name='hour', 
                  value_name='value')


df_long['hour'] = df_long['hour'].str.extract('(\d+)').astype(int)


df_long.to_csv('updated_combined_cleaned_2021-2023_traffic_data.csv', index=False)  

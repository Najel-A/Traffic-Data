import os
import pandas as pd

directory_path = 'traffic_2021'

column_headers = [
    'record_type', 'state_code', 'f_system', 'station_id', 'travel_dir', 
    'travel_lane', 'year_record', 'month_record', 'day_record', 
    'day_of_week', 'hour_00', 'hour_01', 'hour_02', 'hour_03', 
    'hour_04', 'hour_05', 'hour_06', 'hour_07', 'hour_08', 
    'hour_09', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 
    'hour_14', 'hour_15', 'hour_16', 'hour_17', 'hour_18', 
    'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23', 
    'restrictions'
]


for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        
        df = pd.read_csv(file_path, header=None)
        
        df.columns = column_headers
       
        df.to_csv(file_path, index=False)

print("Headers added to all CSV files.")

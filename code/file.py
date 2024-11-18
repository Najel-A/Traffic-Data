import pandas as pd
import os

input_directory = 'traffic_2021'  
output_directory = 'traffic_2021'  

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith('.VOL'):
        
        input_file_path = os.path.join(input_directory, filename)
        df = pd.read_csv(input_file_path, delimiter='|')

        output_file_name = filename.replace('.VOL', '.csv')
        output_file_path = os.path.join(output_directory, output_file_name)
        
        df.to_csv(output_file_path, index=False)

        print(f"Converted {filename} to {output_file_name}")

print("All .vol files have been converted.")

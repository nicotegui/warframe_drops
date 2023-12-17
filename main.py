import pandas as pd
import dask.dataframe as dd

# Read data from CSV file
df = pd.read_csv('raw_missionRewards.csv', header=None, names=['Reward', 'Rarity'], skiprows=1)

# Extract information
rows = []
current_location = None
current_rotation = None

for index, row in df.iterrows():
    line = row['Reward']
    if line.startswith(("Mercury", "Rotation")):
        current_location = line.strip()
    else:
        reward, rarity = [part.strip() for part in line.split(",")]
        rotation = current_rotation if current_rotation else current_location
        rows.append([reward, rarity, rotation])

# Create Dask DataFrame
ddf = dd.from_pandas(pd.DataFrame(rows, columns=['Reward', 'Rarity', 'Rotation/Location']), npartitions=1)

# Write Dask DataFrame to CSV
ddf.to_csv('extracted_data.csv', index=False, single_file=True)

print("Extraction complete. Check 'extracted_data.csv' for the result.")

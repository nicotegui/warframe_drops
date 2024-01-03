import pandas as pd


file_path = 'raw_modByAvatar.csv'
header = 'Mob,Mod,Chance\n'

# Open CSV file
with open('file_path', 'r') as file:
    content = file.read()
    first_line = file.readline()

if first_line == header:
    print("")
else:
    # Add the header row
    with open(file_path, 'r') as file:
        content = file.read()
    
    with open(file_path, 'w') as file:
        file.write(header + content)

# Read data from CSV file with pandas
df = pd.read_csv('file_path')

# Ask for mod to search for
modsearch = input("Search Mod: ")
print("Searching for " + modsearch)

# Search for mod
test = df[(df['Mod'] == 'The Sergeant')]

# Display sources mod is dropped by and their percentages

print("Printing Mods...\n" + test.head() + "\n Search Complete!")


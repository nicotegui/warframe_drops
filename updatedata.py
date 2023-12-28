import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
import io
import time

# Function to process each id 
def process_id(current_id):
    # Find the HTML element with the current id
    current_heading = soup.find('h3', {'id': current_id})

    # Navigate to the table following the heading
    table = current_heading.find_next('table')

    # Create a Pandas dataframe from the HTML table
    html_table = str(table)
    df = pd.read_html(io.StringIO(html_table))[0]

    # Determine the CSV file path
    csv_filename = f'raw_{current_id}.csv'

    # Check if the CSV file already exists
    if os.path.exists(csv_filename):
        try:
            # Remove the existing CSV file
            os.remove(csv_filename)
            print(f"\nExisting CSV file '{csv_filename}' has been deleted.")
        except Exception as e:
            print(f"\nError deleting existing CSV file '{csv_filename}': {e}")

    # Write the entire dataframe to a new CSV file
    try:
        df.to_csv(csv_filename, index=False)
        print(f"\nCSV file '{csv_filename}' has been created.")
    except Exception as e:
        print(f"\nError writing CSV file '{csv_filename}': {e}")


# Start the timer
start_time = time.time()

# Get URL
url = 'https://www.warframe.com/droptables'
response = requests.get(url)

# Parse the HTML content using BS
soup = BeautifulSoup(response.text, 'html.parser')

# Find all <h3> elements with an "id" attribute
h3_elements = soup.find_all('h3', {'id': True})

# Extract the id values from the elements
id_list = [element['id'] for element in h3_elements]

# Process each id using Pandas
for current_id in id_list:
    process_id(current_id)

# Calculate and print the total time taken
total_time = time.time() - start_time
print(f"\nTotal time taken: {total_time:.2f} seconds.")

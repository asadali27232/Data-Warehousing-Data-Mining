import pandas as pd

# Read the data into a DataFrame
df = pd.read_csv('Casualties.csv')

# Check for duplicate IDs
duplicate_ids = df.duplicated('casualties_id', keep=False)

# Filter the DataFrame to show only the duplicate IDs
duplicate_rows = df[duplicate_ids]

# Display the duplicate rows
print(duplicate_rows)
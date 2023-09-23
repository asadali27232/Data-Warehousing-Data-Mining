import pandas as pd

# ----------------------- Crash ----------------------------------
# Read the CSV file
Crash = pd.read_csv('Crash.csv')

# Drop rows with missing values
Crash.dropna(inplace=True)

# Drop duplicate rows
Crash.drop_duplicates(inplace=True)

# Clean "date_time_id" column
Crash = Crash[Crash['date_time_id'] != '2012----']
Crash['date_time_id'] = Crash['date_time_id'].str.replace('-', '', regex=True)

# Drop rows if any value is repeated in that row
Crash = Crash.loc[~Crash.duplicated(keep=False)]

# Clean "crash_id" column
Crash['crash_id'] = Crash['crash_id'].drop_duplicates().dropna()
Crash = Crash.dropna(subset=['crash_id'])

# Remove characters from the first column
Crash[Crash.columns[1]] = Crash[Crash.columns[1]].str.replace(r'[-,.\'()\s]', '', regex=True)

# Remove rows with 'nannan' in the "Crash" column
Crash = Crash[Crash['lat_long'] != 'nannan']

# Save the modified data as a new CSV file
Crash.to_csv('Crash.csv', index=False)

# ------------------ Casualties ----------------------------
# Read the CSV file
Casualties = pd.read_csv('Casualties.csv')

# Clean "casualties_id" column
Casualties['casualties_id'] = Casualties['casualties_id'].drop_duplicates().dropna()

# Save the modified data as a new CSV file
Casualties.to_csv('Casualties.csv', index=False)

# ------------------------ Date Time ----------------------------
# Read the CSV file
DateTime = pd.read_csv('DateTime.csv')

# Clean "date_time_id" column
DateTime['date_time_id'] = DateTime['date_time_id'].str.replace('-', '', regex=True)
DateTime['date_time_id'] = DateTime['date_time_id'].drop_duplicates().dropna()
DateTime = DateTime.dropna(subset=['date_time_id'])

# Save the modified data as a new CSV file
DateTime.to_csv('DateTime.csv', index=False)

# ----------------------- Location --------------------------------
# Read the CSV file with specified data types for columns 5, 6, and 7
Location = pd.read_csv('Location.csv', dtype={ 5: str, 6: str, 7: str, 8: str})

# Drop rows with missing values in the first column
Location.dropna(subset=[Location.columns[1]], inplace=True)

# Drop duplicate rows based on the first column
Location.drop_duplicates(subset=[Location.columns[1]], inplace=True)

# Remove characters from the first column
Location[Location.columns[1]] = Location[Location.columns[1]].str.replace(r'[-,.\'()\s]', '', regex=True)

# Remove rows with 'nannan' in the "Location" column
Location = Location[Location['lat_long'] != 'nannan']

# Clean "lat_long" column
Location['lat_long'] = Location['lat_long'].drop_duplicates().dropna()

# Drop the first column
Location = Location.drop(Location.columns[0], axis=1)

# Save the modified data as a new CSV file
Location.to_csv('Location.csv', index=False)

# --------------------------- Vehicle --------------------------
# Read the CSV file
Vehicles = pd.read_csv('Vehicles.csv')

# Drop rows with missing values in the "vehicles_id" column
Vehicles.dropna(subset=['vehicles_id'], inplace=True)

# Drop duplicate rows based on the "vehicles_id" column
Vehicles.drop_duplicates(subset=['vehicles_id'], inplace=True)

# Clean "vehicles_id" column
Vehicles['vehicles_id'] = Vehicles['vehicles_id'].drop_duplicates().dropna()

# Save the modified data as a new CSV file
Vehicles.to_csv('Vehicles.csv', index=False)

# ----------------------------- Description ---------------------------
# Read the CSV file
Description = pd.read_csv('Description.csv', dtype={3: str,6: str,7: str,8: str,9: str,10: str,11: str,12: str,13: str,14: str,16: str})

# Drop rows with missing values in the "descriptionID" column
Description.dropna(subset=['description_id'], inplace=True)

# Drop duplicate rows based on the "descriptionID" column
Description.drop_duplicates(subset=['description_id'], inplace=True)

# Clean "description_id" column
Description['description_id'] = Description['description_id'].drop_duplicates().dropna()
Description = Description.dropna(subset=['description_id'])


# Drop the first column
Description = Description.drop(Description.columns[0], axis=1)

# Save the modified data as a new CSV file
Description.to_csv('Description.csv', index=False)

print("Crash.csv Cleaned")
print("Casualties.csv Cleaned")
print("Description.csv Cleaned")
print("Location.csv Cleaned")
print("DateTime.csv Cleaned")
print("Vehicle.csv Cleaned")
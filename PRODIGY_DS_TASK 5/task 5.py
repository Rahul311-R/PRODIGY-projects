import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap

# Load the dataset from a local file using just the filename
file_name = 'data 3.csv'  # Update this to your actual CSV file name
data = None  # Initialize data variable

try:
    # Load the dataset with error handling
    data = pd.read_csv(file_name, on_bad_lines='skip', engine='python')
    print(data.head())  # Display the first few rows of the dataset
    print("Columns in the dataset:", data.columns.tolist())  # Print the column names
except Exception as e:
    print(f"An error occurred: {e}")

# Proceed only if data is loaded successfully
if data is not None:
    # Check if the expected columns exist
    print("Checking for expected columns...")
    print(data.columns.tolist())  # Print all column names

    # Check for the presence of required columns
    required_columns = ['Start_Lat', 'Start_Lng', 'Weather_Condition']
    missing_columns = [col for col in required_columns if col not in data.columns]

    if not missing_columns:
        # Data Cleaning
        data.dropna(subset=required_columns, inplace=True)

        # Convert 'Start_Time' to datetime
        data['Start_Time'] = pd.to_datetime(data['Start_Time'])

        # Extract hour and day of the week
        data['Hour'] = data['Start_Time'].dt.hour
        data['Day_of_Week'] = data['Start_Time'].dt.day_name()

        # Accident Hotspots Visualization
        plt.figure(figsize=(12, 6))
        sns.countplot(data=data, x='Day_of_Week', order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        plt.title('Accidents by Day of the Week')
        plt.xlabel('Day of the Week')
        plt.ylabel('Number of Accidents')
        plt.xticks(rotation=45)
        plt.show()

        # Weather Conditions Analysis
        plt.figure(figsize=(12, 6))
        sns.countplot(data=data, y='Weather_Condition', order=data['Weather_Condition'].value_counts().index)
        plt.title('Accidents by Weather Condition')
        plt.xlabel('Number of Accidents')
        plt.ylabel('Weather Condition')
        plt.show()

        # Create a heatmap for accident hotspots
        heatmap_data = data[['Start_Lat', 'Start_Lng']]
        heatmap_data = heatmap_data.dropna()

        # Create a folium map
        accident_map = folium.Map(location=[data['Start_Lat'].mean(), data['Start_Lng'].mean()], zoom_start=10)
        HeatMap(data=heatmap_data, radius=15).add_to(accident_map)

        # Save the map to an HTML file
        accident_map.save('accident_heatmap.html')
        print("Heatmap saved as 'accident_heatmap.html'.")
    else:
        print(f"The following required columns are missing: {missing_columns}")

else:
    print("Data could not be loaded. Please check the file name and format.")

import pandas as pd
from scipy.stats import f_oneway
import matplotlib.pyplot as plt
Education_2018 = pd. read_csv("data/Education_2018.csv")
Education_2022 = pd. read_csv("data/Education_2022.csv")

# Clean up the strings in the 'Label (Grouping)' column for both datasets
Education_2018['Label (Grouping)'] = Education_2018['Label (Grouping)'].str.replace('\xa0','').str.strip()
Education_2022['Label (Grouping)'] = Education_2022['Label (Grouping)'].str.replace('\xa0','').str.strip()

# Print unique values in the 'Label (Grouping)' column after cleaning for both years
print("Unique values in the 'Label (Grouping)' column for 2018:")
print(Education_2018['Label (Grouping)'].unique())

print("\nUnique values in the 'Label (Grouping)' column for 2022:")
print(Education_2022['Label (Grouping)'].unique())

# Selected points
educational_points = [
    "Population 18 to 24 years",
    "Population 25 years and over",
    "Population 25 to 34 years ",
    "Population 35 to 44 years",
    "Population 45 to 64 years ",
    "Population 65 years and over",
    "Racial and ethnic groups",
    "Comparison between 2018 and 2022",
    "Gender differences",
    "Educational attainment by income level"
]

# Dictionary to store selected points and their corresponding values from columns 2 and 3
selected_data_2018 = {}
selected_data_2022 = {}

for point in educational_points:
    # Find the index of the row containing the point for 2018 data
    index_2018 = Education_2018[Education_2018['Label (Grouping)'] == point].index
    if not index_2018.empty:
        index_2018 = index_2018[0]
        # Get the values from columns 2 and 3 for 2018 data
        value_col2_2018 = Education_2018.iloc[index_2018, 1]
        value_col3_2018 = Education_2018.iloc[index_2018, 2]
        # Add the point and its values to the dictionary for 2018 data
        selected_data_2018[point] = {"Value (Column 2)": value_col2_2018, "Value (Column 3)": value_col3_2018}
    
    # Find the index of the row containing the point for 2022 data
    index_2022 = Education_2022[Education_2022['Label (Grouping)'] == point].index
    if not index_2022.empty:
        index_2022 = index_2022[0]
        # Get the values from columns 2 and

      # Print the dictionary for 2018 data
print("2018 Education Data:")
for point, values in selected_data_2018.items():
    print(point)
    print("Value (Column 2) - 2018:", values["Value (Column 2)"])
    print("Value (Column 3) - 2018:", values["Value (Column 3)"])
    print()

# Print the dictionary for 2022 data
print("2022 Education Data:")
for point, values in selected_data_2022.items():
    print(point)
    print("Value (Column 2) - 2022:", values["Value (Column 2)"])
    print("Value (Column 3) - 2022:", values["Value (Column 3)"])
    print()  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Read the CSV files
Education_2018 = pd.read_csv("../data/Education_2018.csv")
Education_2022 = pd.read_csv("../data/Education_2022.csv")

# Define columns of interest
columns_of_interest = ["Madison County, Alabama!!Male!!Estimate", "Madison County, Alabama!!Female!!Estimate"]

# Replace '(X)' and 'N' with NaN
for col in columns_of_interest:
    Education_2018[col] = pd.to_numeric(Education_2018[col], errors='coerce')
    Education_2022[col] = pd.to_numeric(Education_2022[col], errors='coerce')

# Drop rows with NaN values
Education_2018 = Education_2018.dropna(subset=columns_of_interest)
Education_2022 = Education_2022.dropna(subset=columns_of_interest)



# Visualize the data with boxplots
plt.figure(figsize=(10, 6))
plt.boxplot([Education_2018[columns_of_interest[0]], Education_2022[columns_of_interest[0]]], labels=['2018', '2022'])
plt.title('Education Distribution Comparison')
plt.xlabel('Year')
plt.ylabel(columns_of_interest[0])
plt.grid(True)
plt.show()



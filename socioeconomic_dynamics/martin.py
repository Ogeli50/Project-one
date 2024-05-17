import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy import stats
import numpy as np
import seaborn as sns


# Load and clean datasets
emp2018 = pd.read_csv("../data/employment2018.csv")
emp2018['Label (Grouping)'] = emp2018['Label (Grouping)'].str.replace('\xa0', '').str.strip()

emp2022 = pd.read_csv("../data/employment2022.csv")
emp2022['Label (Grouping)'] = emp2022['Label (Grouping)'].str.replace('\xa0', '').str.strip()

# Selected data points
socio_points = [
    "Population 16 years and over",
    "Employed",
    "Unemployed",
    "Median household income (dollars)",
    "With earnings",
    "With Social Security",
    "With retirement income",
    "With Food Stamp/SNAP benefits in the past 12 months",
]

# Function to clean and convert numeric strings to floats
def clean_and_convert(value):
    if isinstance(value, str):
        value = value.replace(',', '')
    try:
        return float(value)
    except ValueError:
        return None

# Function to extract selected data points
def extract_data(df, points):
    selected_data = {}
    for point in points:
        index = df[df['Label (Grouping)'] == point].index
        if not index.empty:
            index = index[0]
            value_col2 = clean_and_convert(df.iloc[index, 1])
            value_col3 = clean_and_convert(df.iloc[index, 2])
            selected_data[point] = {"Value (Column 2)": value_col2, "Value (Column 3)": value_col3}
    return selected_data

# Extract data for 2018 and 2022
data_2018 = extract_data(emp2018, socio_points)
data_2022 = extract_data(emp2022, socio_points)

# Calculate percentage changes
def calculate_percentage_change(data_2018, data_2022):
    percentage_changes = {}
    for key in data_2018:
        value_2018 = data_2018[key]["Value (Column 2)"]
        value_2022 = data_2022.get(key, {}).get("Value (Column 2)", 0)
        if value_2018 and value_2018 != 0:
            change = ((value_2022 - value_2018) / value_2018) * 100
            percentage_changes[key] = change
    return percentage_changes

percentage_changes = calculate_percentage_change(data_2018, data_2022)
print("Percentage Changes:", percentage_changes)

# Create results directory if it doesn't exist
results_dir = "results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Save percentage changes to a CSV file
pd.DataFrame.from_dict(percentage_changes, orient='index', columns=['Percentage Change']).to_csv(os.path.join(results_dir, "percentage_changes.csv"))

# Plotting the percentage changes
keys = list(percentage_changes.keys())
values = list(percentage_changes.values())

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")
colors = sns.color_palette("Set2", len(keys))  # Set a color palette
sns.barplot(x=keys, y=values, palette=colors)

plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Socioeconomic Factors', fontsize=14)
plt.ylabel('Percentage Change (%)', fontsize=14)
plt.title('Percentage Change in Socioeconomic Factors (2018-2022)', fontsize=16)
plt.tight_layout()

# Save the plot as an image file
plt.savefig(os.path.join(results_dir, "percentage_changes.png"))

# Show the plot
plt.show()
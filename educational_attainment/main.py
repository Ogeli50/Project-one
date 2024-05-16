import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind
import os

# Read Data Files
Education_2018 = pd.read_csv("../data\Education_2018.csv")
Education_2022 = pd.read_csv("../data\Education_2022.csv")

# Clean up the strings in the 'Label (Grouping)' column for both datasets
Education_2018['Label (Grouping)'] = Education_2018['Label (Grouping)'].str.replace('\xa0','').str.strip()
Education_2022['Label (Grouping)'] = Education_2022['Label (Grouping)'].str.replace('\xa0','').str.strip()

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

# Create results directory if it doesn't exist
results_dir = "results"
if not os.path.exists(results_dir):
    os.makedirs(results_dir)

# Dictionary to store selected points and their corresponding values from columns 2 and 3
selected_data_2018 = {}
selected_data_2022 = {}

for point in educational_points:
    # Find the index of the row containing the point for 2018 data
    index_2018 = Education_2018[Education_2018['Label (Grouping)'] == point].index
    if not index_2018.empty:
        index_2018 = index_2018[0]
        # Get the values from columns 2 and 3 for 2018 data
        value_col2_2018 = Education_2018.iloc[index_2018, 1].replace('(X)', 'NaN').replace(',', '').strip()
        value_col3_2018 = Education_2018.iloc[index_2018, 2].replace('(X)', 'NaN').replace(',', '').strip()
        # Convert string to float
        value_col2_2018 = float(value_col2_2018) if value_col2_2018 != 'NaN' else np.nan
        value_col3_2018 = float(value_col3_2018) if value_col3_2018 != 'NaN' else np.nan
        # Add the point and its values to the dictionary for 2018 data
        selected_data_2018[point] = {"Value (Column 2)": value_col2_2018, "Value (Column 3)": value_col3_2018}
    
    # Find the index of the row containing the point for 2022 data
    index_2022 = Education_2022[Education_2022['Label (Grouping)'] == point].index
    if not index_2022.empty:
        index_2022 = index_2022[0]
        # Get the values from columns 2 and 3 for 2022 data
        value_col2_2022 = Education_2022.iloc[index_2022, 1].replace('(X)', 'NaN').replace(',', '').strip()
        value_col3_2022 = Education_2022.iloc[index_2022, 2].replace('(X)', 'NaN').replace(',', '').strip()
        # Convert string to float
        value_col2_2022 = float(value_col2_2022) if value_col2_2022 != 'NaN' else np.nan
        value_col3_2022 = float(value_col3_2022) if value_col3_2022 != 'NaN' else np.nan
        # Add the point and its values to the dictionary for 2022 data
        selected_data_2022[point] = {"Value (Column 2)": value_col2_2022, "Value (Column 3)": value_col3_2022}

# Print the dictionaries
print("Selected Data for 2018:")
print(selected_data_2018)
print("\nSelected Data for 2022:")
print(selected_data_2022)

# Perform t-test
values_2018 = [data['Value (Column 2)'] for data in selected_data_2018.values()]
values_2022 = [data['Value (Column 2)'] for data in selected_data_2022.values()]

t_statistic, p_value = ttest_ind(values_2018, values_2022, nan_policy='omit')
print("\nT-statistic:", t_statistic)
print("P-value:", p_value)

# Visualize the data with bar graphs
points = list(selected_data_2018.keys())
bar_width = 0.35
index = np.arange(len(points))
plt.figure(figsize=(10, 6))
plt.bar(index, values_2018, bar_width, label='2018')
plt.bar(index + bar_width, values_2022, bar_width, label='2022')
plt.xlabel('Educational Points')
plt.ylabel('Values')
plt.title('Comparison of Educational Data between 2018 and 2022')
plt.xticks(index + bar_width / 2, points, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Save the plot as an image file
plt.savefig(os.path.join(results_dir, "years_comparison.png"))
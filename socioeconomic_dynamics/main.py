import pandas as pd

# Load the dataset into a DataFrame
# Clean up the strings in the 'Label (Grouping)' column
emp2018 = pd.read_csv("../data/employment2018.csv")
emp2018['Label (Grouping)'] = emp2018['Label (Grouping)'].str.replace('\xa0', '').str.strip()

# Print unique values in the 'Label (Grouping)' column after cleaning
# print(emp2018['Label (Grouping)'].unique())

# Selected points
socio_points_2018 = [
    "Unemployed",
    "Employed",
    "Manufacturing",
    "$50,000 to $74,999",
    "Median household income (dollars)",
    "With earnings",
    "With Social Security",
    "With retirement income",
    "Mean Supplemental Security Income (dollars)",
    "With Food Stamp/SNAP benefits in the past 12 months"
]

# socio_points_2022 = [
#     "Population 16 years and over",
#     "Employed",
#     "Manufacturing",
#     "$50,000 to $74,999",
#     "Median household income (dollars)",
#     "With earnings",
#     "With Social Security",
#     "With retirement income",
#     "Mean Supplemental Security Income (dollars)",
#     "With Food Stamp/SNAP benefits in the past 12 months"
# ]

# # Dictionary to store selected points and their corresponding values from columns 2 and 3
selected_data = {}

for point in socio_points_2018:
    # Find the index of the row containing the point
    index = emp2018[emp2018['Label (Grouping)'] == point].index
    print("Index:", index)
    if not index.empty:
        index = index[0]
        # Get the values from columns 2 and 3 and 4
        value_col2 = emp2018.iloc[index, 1]
        value_col3 = emp2018.iloc[index, 2]
        # Add the point and its values to the dictionary
        selected_data[point] = {"Value (Column 2)": value_col2, "Value (Column 3)": value_col3}

# Print the dictionary
for point, values in selected_data.items():
    print(point)
    print("Value (Column 2):", values["Value (Column 2)"])
    print("Value (Column 3):", values["Value (Column 3)"])
    print()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy import stats
import numpy as np

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

plt.figure(figsize=(10, 5))
sns.barplot(x=keys, y=values)
plt.xticks(rotation=45)
plt.xlabel('Socioeconomic Factors')
plt.ylabel('Percentage Change')
plt.title('Percentage Change in Socioeconomic Factors (2018-2022)')
plt.tight_layout()

# Save the plot as an image file
plt.savefig(os.path.join(results_dir, "percentage_changes.png"))

# Show the plot
plt.show()

# Correlation analysis
values_2018 = [data_2018[point]["Value (Column 2)"] for point in socio_points if data_2018[point]["Value (Column 2)"] is not None]
values_2022 = [data_2022[point]["Value (Column 2)"] for point in socio_points if data_2022[point]["Value (Column 2)"] is not None]
correlation, p_value = stats.pearsonr(values_2018, values_2022)
correlation_results = {"correlation": correlation, "p-value": p_value}
print(f"Correlation between 2018 and 2022 data: correlation = {correlation}, p-value = {p_value}")

# Save correlation results to CSV
pd.DataFrame.from_dict(correlation_results, orient='index').to_csv(os.path.join(results_dir, "correlation_results.csv"))

# Linear regression for trend analysis
years = np.array([2018, 2022])
lin_reg_results = {}
for point in socio_points:
    y_values = np.array([data_2018.get(point, {}).get("Value (Column 2)"), data_2022.get(point, {}).get("Value (Column 2)")])
    print(f"Point: {point}, Y Values: {y_values}")
    if None not in y_values:
        slope, intercept, r_value, p_value, std_err = stats.linregress(years, y_values)
        lin_reg_results[point] = {"slope": slope, "intercept": intercept, "r-squared": r_value**2, "p-value": p_value}
        print(f"Linear regression for {point}: slope = {slope}, intercept = {intercept}, r-squared = {r_value**2}, p-value = {p_value}")

# Save linear regression results to CSV
lin_reg_results_df = pd.DataFrame.from_dict(lin_reg_results, orient='index')
lin_reg_results_df.to_csv(os.path.join(results_dir, "linear_regression_results.csv"))

# Visualize correlation results
plt.figure(figsize=(10, 5))
sns.heatmap([[correlation]], annot=True, xticklabels=['2018-2022'], yticklabels=['Correlation'], cmap='coolwarm')
plt.title('Correlation between 2018 and 2022 Socioeconomic Data')
plt.tight_layout()

# Save the plot as an image file
plt.savefig(os.path.join(results_dir, "correlation_heatmap.png"))

# Show the plot
plt.show()

# Plotting the linear regression lines
plt.figure(figsize=(10, 5))

# Plot actual data points
for point in socio_points:
    y_values = np.array([data_2018.get(point, {}).get("Value (Column 2)"), data_2022.get(point, {}).get("Value (Column 2)")])
    if None not in y_values:
        plt.scatter([2018, 2022], y_values, label=point)

# Plot linear regression lines
for point in socio_points:
    y_values = np.array([data_2018.get(point, {}).get("Value (Column 2)"), data_2022.get(point, {}).get("Value (Column 2)")])
    if None not in y_values:
        slope, intercept, _, _, _ = stats.linregress([2018, 2022], y_values)
        plt.plot([2018, 2022], [intercept + slope * 2018, intercept + slope * 2022], label=f"{point} Regression")

plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Linear Regression for Socioeconomic Factors (2018-2022)')

# Place legend beneath the chart
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), shadow=True, ncol=2)
plt.tight_layout()

# Save the plot as an image file
plt.savefig(os.path.join(results_dir, "linear_regression_plot.png"))

# Show the plot
plt.show()



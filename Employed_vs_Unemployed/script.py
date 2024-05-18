
import pandas as pd
import matplotlib.pyplot as plt

# URL to the raw CSV file on GitHub
data = "https://raw.githubusercontent.com/Ogeli50/Project-one/main/Employed_vs_Unemployed/file-2.csv"

# Display the DataFrame

df = pd.read_csv(data)

# Display data

print(df)


# In[3]:


# Ensure that essential columns exist
required_columns = ['Year', 'Value']
if not all(column in df.columns for column in required_columns):
    raise ValueError(f"Missing required columns: {required_columns}")

# Ensure the 'Value' column is numeric and handle non-numeric values
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Drop rows with any NaN values in required columns
df.dropna(subset=required_columns, inplace=True)

# Separate the data by year
years = df['Year'].unique()
print(f"Unemployment Rates by Year: {years}")

# Create a summary DataFrame to store the statistics
summary = pd.DataFrame(columns=['Year', 'Mode', 'Median', 'Range'])

# Calculate the mode, median, and range for each year
for year in years:
    yearly_data = df[df['Year'] == year]
    
    # Select only the 'Value' column for calculations
    values = yearly_data['Value']
    
    # Calculate mode (most frequent value)
    mode = values.mode().iloc[0] if not values.mode().empty else None
    
    # Calculate median
    median = values.median()
    
    # Calculate range (max - min)
    data_range = values.max() - values.min()
    
    # Create a DataFrame for the current year's statistics
    current_summary = pd.DataFrame({
        'Year': [year],
        'Mode': [mode],
        'Median': [median],
        'Range': [data_range]
    })
    
    # Only concatenate if the current_summary is not empty
    if not current_summary.empty:
        summary = pd.concat([summary, current_summary], ignore_index=True)

# Display the summary DataFrame
print("Summary DataFrame:")
print(summary)


# In[4]:


# Plot the statistics for visualization

summary.set_index('Year', inplace=True)
summary.plot(kind='bar', subplots=True, layout=(3, 1), figsize=(10, 12), legend=False, title='Unemployment Rates Statistics by Year')
plt.tight_layout()
plt.show()


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# URL to the raw CSV file on GitHub
data_url = "https://raw.githubusercontent.com/Ogeli50/Project-one/aa80c6bd5f7dabd01043f89556f11c0474837e35/Employed_vs_Unemployed/file.csv"

# Load the DataFrame
df = pd.read_csv(data_url)

# Columns to check
required_columns = ['Year', 'Value']

# Ensure the 'Value' column is numeric and handle non-numeric values
if 'Value' in df.columns:
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Drop rows with any NaN values in required columns
df.dropna(subset=required_columns, inplace=True)

# Group the data by 'Year' and calculate the mean 'Value' for each year
yearly_summary = df.groupby('Year')['Value'].mean().reset_index()

# Create a line chart of 'Year' vs. mean 'Value'
plt.figure(figsize=(10, 6))
plt.plot(yearly_summary['Year'], yearly_summary['Value'], marker='o', linestyle='-', color='red', label='Value')
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Alabama Employment Rates by Year in Thousands')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:

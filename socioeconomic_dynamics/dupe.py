# This script observes a primary/main comma seperated file and a secondary comma seperated file 
# and makes the changes that were done manually to the primary CSV file to the secondary CSV file. 

import os
import pandas as pd

def update_secondary(primary_file, secondary_file):
    # Read primary/main and secondary/to be copied to CSV files
    primary_df = pd.read_csv(primary_file)
    secondary_df = pd.read_csv(secondary_file)

    # Perform drops or deletes according to the primary file updating the secondary file.
    updated_secondary_df = secondary_df.merge(primary_df, indicator=True, how='outer').query('_merge=="right_only"').drop(columns=['_merge'])

    # Get the filename without extension from the primary file
    primary_filename = os.path.splitext(os.path.basename(primary_file))[0]

    # Construct the new filename for the modified secondary file
    modified_secondary_filename = f"data/{primary_filename}_modified.csv"

    # Write updated secondary file with the new filename
    updated_secondary_df.to_csv(modified_secondary_filename, index=False)
    print("Secondary file updated successfully.")

if __name__ == "__main__":
    primary_file = "data/primary/employment2018.csv"
    secondary_file = "data/secondary/ACSDP1Y2018.DP03-2024-05-09T012103.csv"
    update_secondary(primary_file, secondary_file)
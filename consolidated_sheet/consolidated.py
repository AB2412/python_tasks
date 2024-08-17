import os
import pandas as pd

def consolidate_xlsx_files(directory, output_file):
    """
    Consolidate all xlsx files in the specified directory into a single Excel sheet without repeating headers.
    
    Args:
    directory (str): The directory containing the xlsx files.
    output_file (str): The name of the output file.
    """
    all_data = []

    # Loop through all files in the directory
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):
            file_path = os.path.join(directory, file)
            # Read each Excel file
            df = pd.read_excel(file_path)
            # Append data to the list
            all_data.append(df)

    # Concatenate all dataframes in the list
    consolidated_data = pd.concat(all_data, ignore_index=True)

    # Write the consolidated data to a new Excel file
    consolidated_data.to_excel(output_file, index=False)

# Example usage
directory = '/home/areeba/python_practice/consolidated_sheet'
output_file = 'consolidated_data.xlsx'
consolidate_xlsx_files(directory, output_file)

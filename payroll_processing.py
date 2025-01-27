#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the output directory
BASE_DIR = r"C:\GIT\Innovative\employee-payroll-processing"
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

# Ensure the output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_files(database_path, current_path):
    # Define transaction codes
    transaction_codes = {
        'Day Shift': 100,
        'Night Shift at 1.15x': 101,
        'Sunday at 1.5x': 102,
        'Sick Leave': 103,
        'IOD': 106,
        'Leave Pay': 105,
        'Family \\ Comp': 108,
        'Public Holiday at 1x': 104
    }

    # Load files
    try:
        print("Loading files...")
        database = pd.read_excel(database_path)
        current = pd.read_excel(current_path)
        print("Files loaded successfully")
    except Exception as e:
        return None, f"Error loading files: {str(e)}"
    
    # Ensure 'work number' is the first column in the database
    if 'work number' in database.columns:
        cols = list(database.columns)
        cols.insert(0, cols.pop(cols.index('work number')))
        database = database[cols]
    else:
        return None, "'work number' column not found in the database."

    # Rename columns in the current DataFrame
    if 'name' in current.columns:
        name_idx = list(current.columns).index('name')
        current = current.iloc[:, name_idx:]
        current.columns = current.columns.str.replace(' ', '_').str.replace('\n', '')
    else:
        return None, "'name' column not found in the current DataFrame."

    # Merge the two DataFrames
    try:
        print("Merging files...")
        merged_data = pd.merge(database, current, on='name', how='outer', indicator=True, suffixes=('_database', '_current'))
        print("Files merged successfully")
    except Exception as e:
        return None, f"Error merging files: {str(e)}"

    # Check for missing employee hours
    missing_employees = database[~database['name'].isin(current['name'])]
    if not missing_employees.empty:
        missing_employees_df = missing_employees[['work number', 'name']].copy()
        missing_employees_df.rename(columns={'work number': 'employee code', 'name': 'Name'}, inplace=True)
        missing_employees_df['Resigned'] = ''
        missing_employees_df['Absent'] = ''
        
        # Save missing employees to Excel
        missing_employees_path = os.path.join(OUTPUT_DIR, 'employees_without_hours.xlsx')
        missing_employees_df.to_excel(missing_employees_path, index=False)
        print(f"Missing employees report saved to: {missing_employees_path}")
    else:
        print("No missing employee hours found.")

    # Check for new employees
    new_employees = merged_data[merged_data['_merge'] == 'right_only'].copy()
    new_employees.drop(columns='_merge', inplace=True)
    if not new_employees.empty:
        database = pd.concat([database, new_employees], ignore_index=True)
        database.to_excel(os.path.join(BASE_DIR, 'database.xlsx'), index=False)
        return None, 'New employees found. Database updated.'

    # Check for duplicates in 'work number'
    duplicates = merged_data['work number'].duplicated(keep=False)
    if duplicates.any():
        duplicate_work_numbers = merged_data.loc[duplicates, 'work number'].unique()
        print(f"Please check duplicate employee codes: {', '.join(map(str, duplicate_work_numbers))}")

    # Create the final DataFrame with required columns
    new_data = pd.DataFrame(columns=['work number', 'name', 'Hours', 'Transaction Code'])

    for column, code in transaction_codes.items():
        col_name = column.replace(' ', '_').replace('\\', '').replace('\n', '')
        if col_name in merged_data.columns:
            temp_df = merged_data[['work number', 'name', col_name]].copy()
            temp_df.rename(columns={col_name: 'Hours'}, inplace=True)
            temp_df['Transaction Code'] = code
            new_data = pd.concat([new_data, temp_df], ignore_index=True)

    # Remove rows with NaN or zero Hours
    new_data.dropna(subset=['Hours'], inplace=True)
    new_data['Hours'] = pd.to_numeric(new_data['Hours'], errors='coerce').fillna(0)
    new_data = new_data[new_data['Hours'] > 0]

    # Save the final payroll data to Excel
    payroll_data_path = os.path.join(OUTPUT_DIR, 'payroll_data.xlsx')
    new_data.to_excel(payroll_data_path, index=False)
    print(f"Payroll data saved to: {payroll_data_path}")

    # Visualizations
    if not new_data.empty:
        # Total hours per employee
        total_hours = new_data.groupby('name')['Hours'].sum().sort_values(ascending=False)
        total_hours_plot_path = os.path.join(OUTPUT_DIR, 'total_hours_per_employee.png')
        plt.figure(figsize=(10, 6))
        total_hours.plot(kind='bar', color='skyblue')
        plt.title('Total Hours Worked Per Employee')
        plt.ylabel('Total Hours')
        plt.xlabel('Employee Name')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(total_hours_plot_path)
        plt.show()
        print(f"Total hours plot saved to: {total_hours_plot_path}")

        # Hours by transaction code
        hours_by_code = new_data.groupby('Transaction Code')['Hours'].sum()
        hours_by_code_plot_path = os.path.join(OUTPUT_DIR, 'hours_by_transaction_code.png')
        plt.figure(figsize=(10, 6))
        hours_by_code.plot(kind='pie', autopct='%1.1f%%', startangle=140, cmap='viridis')
        plt.title('Hours Worked by Transaction Code')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(hours_by_code_plot_path)
        plt.show()
        print(f"Transaction code pie chart saved to: {hours_by_code_plot_path}")

    return new_data, 'Processing completed successfully.'

# Example usage
database_path = os.path.join(BASE_DIR, 'data', 'database.xlsx')
current_path = os.path.join(BASE_DIR, 'data', 'current.xlsx')
dataframe, message = process_files(database_path, current_path)
print(message)



# In[ ]:





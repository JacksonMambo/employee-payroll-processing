# employee-payroll-processing
A Python-based tool designed to automate the preparation of employee field data for seamless import into Sage VIP Payroll software. This script processes employee records from timesheets, identifies discrepancies, and formats the data into Sage-compatible reports, ensuring efficiency and accuracy in payroll management.

Features:

    Data Merging: Combines employee databases and field timesheets into a unified dataset.
    Discrepancy Detection:
        Identifies missing employee hours.
        Detects new employees in the timesheets not present in the database.
    Sage VIP Payroll Compatibility: Generates a properly formatted file (payroll_data.xlsx) ready for import into Sage VIP Payroll software.
    Reporting:
        Creates employees_without_hours.xlsx for employees with no recorded hours.
        Visualizes total hours worked and transaction code breakdown.
    Error Handling: Ensures smooth processing even with missing or inconsistent data.

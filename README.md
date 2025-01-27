# Employee Payroll Processing

## Description
A Python-based tool designed to automate the preparation of employee field data for seamless import into Sage VIP Payroll software. This script processes employee records from timesheets, identifies discrepancies, and formats the data into Sage-compatible reports, ensuring efficiency and accuracy in payroll management.

---

## Features
- **Data Merging:** Combines employee databases and field timesheets into a unified dataset.
- **Discrepancy Detection:**
  - Identifies missing employee hours.
  - Detects new employees in the timesheets not present in the database.
- **Sage VIP Payroll Compatibility:** Generates a properly formatted file (`payroll_data.xlsx`) ready for import into Sage VIP Payroll software.
- **Reporting:**
  - Creates `employees_without_hours.xlsx` for employees with no recorded hours.
  - Visualizes total hours worked and transaction code breakdown.
- **Error Handling:** Ensures smooth processing even with missing or inconsistent data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-payroll-processing.git
   cd employee-payroll-processing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Place your input files in the `data/` directory:
   - `database.xlsx`: Contains the employee database.
   - `current.xlsx`: Contains the timesheet records.

2. Run the script:
   ```bash
   python payroll_processing.py
   ```

3. Output files:
   - `payroll_data.xlsx`: Final data for Sage VIP Payroll import.
   - `employees_without_hours.xlsx`: Report of employees without recorded hours.
   - Visualizations:
     - `total_hours_per_employee.png`
     - `hours_by_transaction_code.png`

---

## Results

### Example Visualizations:
- **Hours Distribution by Transaction Code**:
  ![hours_by_transaction_code](https://github.com/user-attachments/assets/ac74a007-888d-4bbb-a747-107937f3169e)
          
- **Total Hours Worked by Employees**:
 ![total_hours_per_employee](https://github.com/user-attachments/assets/34a5493c-efde-4207-bf76-3adcfd945390)
         
---

## File Structure
```
employee-payroll-processing/
├── README.md               # Project overview
├── payroll_processing.py   # Main script
├── requirements.txt        # Python dependencies
├── LICENSE                 # License file
├── data/                   # Input files directory
│   ├── database.xlsx
│   ├── current.xlsx
├── tests/                  # Unit tests
│   ├── test_payroll_processing.py
├── .gitignore              # Ignored files
└── docs/                   # Additional documentation
    ├── architecture.md
    ├── workflow.md
```

---

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Running Tests

1. Install `pytest`:
   ```bash
   pip install pytest
   ```
2. Run the tests:
   ```bash
   pytest tests/
   ```




# SOC Alert Analyzer

A Python-based security alert filtering and reporting project developed as part of my hands-on cybersecurity learning.

## Project Overview

This project uses simulated security alerts to demonstrate how Python can identify records that meet specific investigation criteria.

The analyzer filters open, high-severity malware alerts, summarizes alert categories, and exports matching records to a CSV report.

## Features

- Filters alerts using multiple conditions
- Identifies matching alerts by unique ID
- Counts alerts by category
- Displays formatted investigation results
- Exports matching alerts to CSV
- Supports manual testing of detection logic

## Technologies

- Python 3
- Python CSV standard library
- Visual Studio Code
- Markdown

## How to Run

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Open a terminal in the project directory.
4. Run:

   `python alert_analyzer.py`

5. Review the terminal output and generated `investigation_report.csv`.

No external Python packages are required.

## Testing

### Test Case 001: Severity Change Detection

The severity of simulated alert ALT-003 was changed from Low to High.

Expected result: The number of qualifying alerts increases from two to three.

Actual result: Three alerts were identified and exported successfully.

### Test Result: PASS

See `TEST_RESULTS.md` for the documented test procedure.

## Project Limitations

- Uses simulated alerts rather than live SOC data
- Relies on predefined alert categories and conditions
- Does not determine whether an alert is a confirmed security incident
- Does not currently ingest SIEM logs or external data sources

## Skills Demonstrated

- Python dictionaries, loops, and conditional logic
- Rule-based security alert filtering
- Data summarization
- CSV report generation
- Manual testing and output validation

## Future Improvements

Potential enhancements include input validation, automated tests, and importing alerts from external CSV files.

## Disclaimer

This is an educational cybersecurity project using fictional security alert data. It is not a production SOC detection system.

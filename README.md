# ETL_Pipeline

This project contains ETL (Extract, Transform, Load) pipelines for processing banking and economic data from web sources and CSV files, transforming them, and loading the results into CSV files and SQLite databases.

## Folder Structure

```
ETL_Pipeline/
│
├── test.py
└── WorldBanks/
    ├── Banks.db
    ├── etl_code.py
    ├── etl_code2.py
    ├── etl_project_log.txt
    ├── exchange_rate.csv
    ├── Largest_banks_by_MC.csv
    ├── Largest_banks.csv
    └── World_Economies.db
```

## Contents

- **test.py**: Simple test script.
- **WorldBanks/etl_code.py**: ETL pipeline for Country-GDP data.
- **WorldBanks/etl_code2.py**: ETL pipeline for Bank data.
- **WorldBanks/exchange_rate.csv**: Exchange rates for currency conversion.
- **WorldBanks/Largest_banks_by_MC.csv**: Output CSV from `etl_code2.py`.
- **WorldBanks/Largest_banks.csv**: Output CSV from `etl_code.py`.
- **WorldBanks/Banks.db** and **WorldBanks/World_Economies.db**: SQLite databases for storing processed data.
- **WorldBanks/etl_project_log.txt**: Log file for ETL process steps.

## How to Run

1. Ensure you have Python 3.x installed.
2. Install required libraries:
    ```sh
    pip install pandas numpy beautifulsoup4 requests
    ```
3. Run the ETL scripts:
    ```sh
    python WorldBanks/etl_code.py
    python WorldBanks/etl_code2.py
    ```
4. Outputs will be generated in the `WorldBanks` folder as CSV files and SQLite databases.

## Notes

- The ETL scripts fetch data from archived Wikipedia pages and process them.
- Exchange rates are read from `exchange_rate.csv` for currency conversion.
- Logs are written to `etl_project_log.txt`.

## License

This project is
# Web Scraping ETL Pipeline for Bank Data 🏦

This project is a practical demonstration of a complete **ETL (Extract, Transform, Load)** pipeline built in Python. It extracts data on the world's largest banks from a Wikipedia archive, transforms the data by converting financial figures into multiple currencies, and loads it into a CSV file and a local SQLite database for querying and analysis.

## Features

-   **Data Extraction**: Scrapes bank names and market capitalization from an archived Wikipedia page using `requests` and `BeautifulSoup`.
-   **Data Transformation**: Reads exchange rates from a local CSV and converts market capitalization from USD to British Pounds (GBP), Euros (EUR), and Indian Rupees (INR) using `pandas` and `numpy`.
-   **Dual Data Loading**: Loads the transformed data into both a structured **SQLite database** and a flat **CSV file**.
-   **Automated Logging**: Tracks the start and end of each ETL stage with timestamps in a dedicated log file.
-   **Data Verification**: Automatically runs sample SQL queries on the newly created database to verify the data integrity and demonstrate usability.

## Folder Structure
Of course. Here is a complete, raw README.md file tailored for your project. You can copy this entire block of text and paste it directly into your README.md file.

It includes all the sections we discussed, with the folder structure and commands updated to perfectly match your project.

Markdown

# Web Scraping ETL Pipeline for Bank Data 🏦

This project is a practical demonstration of a complete **ETL (Extract, Transform, Load)** pipeline built in Python. It extracts data on the world's largest banks from a Wikipedia archive, transforms the data by converting financial figures into multiple currencies, and loads it into a CSV file and a local SQLite database for querying and analysis.

## Features

-   **Data Extraction**: Scrapes bank names and market capitalization from an archived Wikipedia page using `requests` and `BeautifulSoup`.
-   **Data Transformation**: Reads exchange rates from a local CSV and converts market capitalization from USD to British Pounds (GBP), Euros (EUR), and Indian Rupees (INR) using `pandas` and `numpy`.
-   **Dual Data Loading**: Loads the transformed data into both a structured **SQLite database** and a flat **CSV file**.
-   **Automated Logging**: Tracks the start and end of each ETL stage with timestamps in a dedicated log file.
-   **Data Verification**: Automatically runs sample SQL queries on the newly created database to verify the data integrity and demonstrate usability.

## Folder Structure
```
ETL_Pipelines/
├── .gitignore
├── https://www.google.com/search?q=LICENSE
├── README.md
├── requirements.txt
├── database/
│   └── Banks.db
├── data/
│   ├── exchange_rate.csv
│   └── Largest_banks_by_MC.csv
├── logs/
│   └── etl_project_log.txt
└── src/
└── etl_code.py
```

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Sam3305/ETL_Pipelines.git](https://github.com/Sam3305/ETL_Pipelines.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd ETL_Pipelines
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the ETL script:**
    ```bash
    python src/etl_code.py
    ```

### Script Execution Flow

When you run the script, it will perform the following actions automatically:
1.  **Extracts** data from the archived Wikipedia page.
2.  **Transforms** the dataset by cleaning values and adding market cap in GBP, EUR, and INR.
3.  **Loads** the final data into `database/Banks.db` and `data/Largest_banks_by_MC.csv`.
4.  **Logs** progress for each stage in `logs/etl_project_log.txt`.
5.  **Runs** and prints the output of three sample SQL queries to the terminal for immediate verification.

## Requirements

- Python 3.7+
- pandas
- numpy
- beautifulsoup4
- requests

You can install all necessary packages by running `pip install -r requirements.txt`. The content of the `requirements.txt` file should be:

```txt
# requirements.txt
pandas
numpy
beautifulsoup4
requests
```

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [Web Archive](web.archive.org)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Wikipedia](en.wikipedia.org/wiki/List_of_largest_banks)
- [Coursera](https://www.coursera.org/)
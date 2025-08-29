# Code for ETL operations on Country-GDP data

# Importing the required libraries
import numpy as np
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import sqlite3
import requests


def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + " : " + message + "\n")


def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page, 'html.parser')

    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')

    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            if col[1].find('a') is not None and '-' not in col[2]:
                data_dict = {
                    "Name": col[1].a.get_text(strip=True),  # FIXED
                    "MC_USD_Billion": col[2].get_text(strip=True)
                }
                df1 = pd.DataFrame([data_dict])
                df = pd.concat([df, df1], ignore_index=True)

    # typecasting Market Cap column
    Mcap_list = df["MC_USD_Billion"].tolist()
    Mcap_list = [float(str(x).replace(",", "").strip()) for x in Mcap_list]
    Mcap_list = [np.round(x, 2) for x in Mcap_list]
    df["MC_USD_Billion"] = Mcap_list

    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # read from csv file
    exchangeRate_df = pd.read_csv(csv_path, index_col="Currency")
    Ex_GBP = exchangeRate_df.loc["GBP", "Rate"]
    Ex_EUR = exchangeRate_df.loc["EUR", "Rate"]
    Ex_INR = exchangeRate_df.loc["INR", "Rate"]

    # adding new columns
    df["MC_GBP_Billion"] = (df["MC_USD_Billion"] * Ex_GBP).round(2)
    df["MC_EUR_Billion"] = (df["MC_USD_Billion"] * Ex_EUR).round(2)
    df["MC_INR_Billion"] = (df["MC_USD_Billion"] * Ex_INR).round(2)

    return df


def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path, index=False)


def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)


def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print("\nRunning Query:", query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)


# ---------------- MAIN SCRIPT ---------------- #

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
output_csv_path = './Largest_banks.csv'
exchange_csv = './exchange_rate.csv'

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
print("Extract Output:\n")
print(df)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, exchange_csv)
print("Transfrom Output:\n")
print(df)
log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, output_csv_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running queries')

query_statement1 = "SELECT * FROM Largest_banks"
run_query(query_statement1, sql_connection)

query_statement2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
run_query(query_statement2, sql_connection)

query_statement3 = "SELECT Country FROM Largest_banks LIMIT 5"
run_query(query_statement3, sql_connection)

log_progress('Process Complete.')

sql_connection.close()

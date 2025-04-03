# Customer Transaction Aggregation
This project processes customer transactions, info, and product, cleans and transforms the data, 
and aggregates customer revenue into a SQLite database for further analysis.


## Overview
The project involves the following steps:
1. **Data Cleansing & Transformation**: Customer, transaction, and product data are cleaned and transformed using the `CustomerTransactionsCleaner`.
2. **Data Aggregation**: Aggregated customer revenue is calculated and stored in an SQLite database.
3. **Verification & Table Listing**: Functions are provided to verify the results of the aggregation and list all tables in the database.

## Modules

- **SQLiteConnector**: Handles connections and queries to the SQLite database.
- **CustomerTransactionsCleaner**: Cleans and transforms the input data (customers, transactions, and products) to prepare for aggregation.
- **DataAggregation**: Aggregates customer revenue and stores the results in the database.


## Usage

1. Prepare mock data files (CSV format) for customers, transactions, and products.
   - `mock_data/customers.csv`
   - `mock_data/transactions.csv`
   - `mock_data/products.csv`

2. Run the script:

```bash
python main.py
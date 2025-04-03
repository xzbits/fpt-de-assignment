import sqlite3
import pandas as pd
from SQLiteConnector import SQLiteConnector
from CleansingTransformation import CustomerTransactionsCleaner
from DataAggregation import DataAggregation


if __name__ == "__main__":
    cleaner = CustomerTransactionsCleaner(
        customers_filepath='mock_data/customers.csv',
        transactions_filepath='mock_data/transactions.csv',
        products_filepath='mock_data/products.csv'
    )

    cleaner.executing_pipelines()

    db_path = "sqlite_customer_transaction.db"
    aggregator = DataAggregation(db_filepath=db_path)
    aggregator.aggregate_customer_revenue()


    def verify_customer_revenue():
        db_connector = SQLiteConnector(db_path)
        query = "SELECT * FROM customer_revenue;"
        db_connector.connect()
        db_connector.cursor.execute(query)
        rows = db_connector.cursor.fetchall()

        for row in rows:
            print(row)

        db_connector.close()

    def list_all_tables(db_path: str):
        db_connector = SQLiteConnector(db_path)

        query = "SELECT name FROM sqlite_master WHERE type='table';"

        tables = db_connector.fetch_all(query, params=None)

        db_connector.close()

        return [table[0] for table in tables]


    # Example usage
    db_path = 'sqlite_customer_transaction.db'  # Replace with your database path
    print("Tables in the database:", list_all_tables(db_path))

    verify_customer_revenue()
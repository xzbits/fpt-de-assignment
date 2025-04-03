import pandas as pd
import sqlite3
import re
from datetime import datetime


class CustomerTransactionsCleaner:
    def __init__(self, customers_filepath, transactions_filepath, products_filepath,
                 email_pattern=None, date_pattern=None):
        # Filepath
        self.customer_filepath = customers_filepath
        self.transactions_filepath = transactions_filepath
        self.products_filepath = products_filepath

        # Pattern info
        self.email_pattern = email_pattern
        self.date_pattern = date_pattern

        # DF initiation
        self.customers_df = pd.read_csv(self.customer_filepath)
        self.transactions_df = pd.read_csv(self.customer_filepath)
        self.products_df = pd.read_csv(self.customer_filepath)

    def load_csv(self):
        """Load CSV files into Pandas dataframe"""
        self.customers_df = pd.read_csv(self.customer_filepath)
        self.transactions_df = pd.read_csv(self.transactions_filepath)
        self.products_df = pd.read_csv(self.products_filepath)

    @staticmethod
    def is_valid_email(email, email_pattern):
        """Check valid email string"""
        if email_pattern is None:
            email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(email_pattern, str(email)))

    @staticmethod
    def is_valid_date(date, date_pattern):
        """Check valid date string"""
        if date_pattern is None:
            date_pattern = "%Y-%m-%d"

        try:
            datetime.strptime(date, date_pattern)
            return True
        except ValueError:
            return False

    @staticmethod
    def standardize_category(category):
        return str(category).strip().lower()

    def clean_customers(self):
        self.customers_df = self.customers_df[self.customers_df['email'].apply(lambda email: self.is_valid_email(email, self.email_pattern))]
        self.customers_df.dropna(subset=['email'], inplace=True)

    def clean_transactions(self):
        self.transactions_df = self.transactions_df[self.transactions_df['transaction_date'].apply(lambda date: self.is_valid_date(date, self.date_pattern))]
        self.transactions_df.drop_duplicates(inplace=True)

    def standardize_categories(self):
        self.products_df['category'] = self.products_df['category'].apply(self.standardize_category)

    def load_data(self, db_path):
        conn = sqlite3.connect(db_path)

        self.customers_df.to_sql('customers', conn, if_exists='append', index=False)
        self.transactions_df.to_sql('transactions', conn, if_exists='append', index=False)
        self.products_df.to_sql('products', conn, if_exists='append', index=False)

        conn.commit()
        conn.close()

    def executing_pipelines(self):
        # Extracting data
        self.load_csv()

        # Transforming data
        self.standardize_categories()
        self.clean_customers()
        self.clean_transactions()

        # Loading data
        self.load_data("sqlite_customer_transaction.db")

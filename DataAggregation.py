from SQLiteConnector import SQLiteConnector

class DataAggregation:
    def __init__(self, db_filepath: str):
        self.db_connector = SQLiteConnector(db_filepath)

    def aggregate_customer_revenue(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS customer_revenue (
            customer_id INTEGER PRIMARY KEY,
            total_revenue REAL
        );
        """
        insert_data_query = """
        INSERT INTO customer_revenue (customer_id, total_revenue)
        SELECT customer_id, SUM(transaction_amount)
        FROM transactions
        GROUP BY customer_id;
        """

        # Execute the queries
        self.db_connector.execute_query(create_table_query)
        self.db_connector.execute_query(insert_data_query)
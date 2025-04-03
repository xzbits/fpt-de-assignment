import sqlite3
from typing import Any, Optional, Tuple, List

class SQLiteConnector:
    def __init__(self, sqlite_db_filepath: str):
        self.sqlite_db_filepath = sqlite_db_filepath
        self.connection = None
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.sqlite_db_filepath)
            self.cursor = self.connection.cursor()


    def execute_query(self, query: str, params: Optional[Tuple[Any, ...]] = None) -> None:
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        self.connection.commit()

    def fetch_all(self, query: str, params: Optional[Tuple[Any, ...]]) -> List[Tuple]:
        self.connect()
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

        return self.cursor.fetchall()

    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            self.connection = None
            self.cursor = None
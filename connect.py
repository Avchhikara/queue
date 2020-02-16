import psycopg2
from psycopg2 import Error


class PostgresDB:
    def __init__(self):
        super().__init__()
        self.cursor = None
        self.connection = None

    def __enter__(self):
        try:
            connection = psycopg2.connect(
                user="avnish",
                password="",
                host="127.0.0.1",
                port="5432",
                database="queues"
            )
            cursor = connection.cursor()
            self.cursor = cursor
            self.connection = connection
        except (Exception, psycopg2.DatabaseError) as error:
            raise Error(error)

        return self.cursor

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        self.connection.close()

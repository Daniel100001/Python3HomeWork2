import sqlite3
from database import sql_queries


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("dataBase connected successfully")

        self.connection.execute(sql_queries.create_user_table_query)
        self.connection.commit()

    def sql_insert_users(self, telegram_id,
                         username, first_name, last_name):
        self.cursor.execute(sql_queries.start_insert_user_query,
                (None, telegram_id, username, first_name, last_name)
                            )
        self.connection.commit()

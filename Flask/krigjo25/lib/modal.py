#   Import the responsories
import sqlite3 as sql

class SQL():
    def __init__(self, database) -> None:

        #   Initializing contact with the database
        self.conn = sql.connect(database)

        #   Initializing the sql cursor
        self.cur = self.conn.cursor()
        
        print('connected to sqlite')
        return
    
    def selectRecord(self, table, *columns):

        # Ensure the columns is false
        if bool(columns):
            pass
        else:
            columns = "*"

        #   Initialize the statement to execute
        query =f"SELECT {columns} FROM {table};"

        #   Execute the SQL statement
        self.cur.execute(query)

        #   Close connection
        self.conn.close()

        return 

class Apis():
    pass
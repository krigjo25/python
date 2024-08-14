#   Import the responsories
import sqlite3 as sql

class SQL():
    def __init__(self, database) -> None:
        conn = sql.connect(database)
        self.cur = conn.cursor()
        
        print('connected to sqlite')
        
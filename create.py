import sqlite3

conn = sqlite3.connect('analytics.db')

try:
    conn.execute(
            '''
                CREATE TABLE monitor
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_date NUMERIC,
                type TEXT NOT NULL,
                status TEXT NOT NULL,
                reason TEXT NOT NULL,
                elapsed REAL NOT NULL
            )
            '''
                 )

    print("Table created successfully")

except:
    pass

conn.close()

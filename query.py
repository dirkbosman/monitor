import sqlite3

conn = sqlite3.connect('analytics.db')

cur = conn.execute('select * from monitor')

results = [dict(id=row[0],
            created_date=row[1],
            type=row[2],
            status=row[3],
            reason=row[4],
            elapsed=row[5],
            ) for row in cur.fetchall()
       ]

print(results)

conn.close()


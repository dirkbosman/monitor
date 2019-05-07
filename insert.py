import sqlite3
import requests
from datetime import datetime

# Create Endpoints
analytics = requests.get("https://analytics.spotify.com/")
labs = requests.get("https://labs.spotify.com/")
docs = requests.get("https://developer.spotify.com/")
music = requests.get("https://open.spotify.com/browse/featured")

# Connect To DB
time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
conn = sqlite3.connect('analytics.db')

# Insert Variables' Values Into DB
print("Inserting records into monitor-table")
try:
    conn.execute("INSERT INTO monitor (id, created_date, type, status, reason, elapsed) VALUES (?,?,?,?,?,?)",
                 [None, time, "analytics", analytics.status_code, analytics.reason,
                  analytics.elapsed.total_seconds()]
                 )
    conn.execute("INSERT INTO monitor (id, created_date, type, status, reason, elapsed) VALUES (?,?,?,?,?,?)",
                 [None, time, "labs", labs.status_code, labs.reason,
                  labs.elapsed.total_seconds()]
                 )
    conn.execute("INSERT INTO monitor (id, created_date, type, status, reason, elapsed) VALUES (?,?,?,?,?,?)",
                 [None, time, "docs", docs.status_code, docs.reason, docs.elapsed.total_seconds()]
                 )
    conn.execute("INSERT INTO monitor (id, created_date, type, status, reason, elapsed) VALUES (?,?,?,?,?,?)",
                 [None, time, "music", music.status_code, music.reason, music.elapsed.total_seconds()]
                 )
    print("Inserted successfully")
except:
    pass

conn.commit()

print("Committed successfully")

conn.close()

